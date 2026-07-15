#!/usr/bin/env python3
"""Batch-download songs from YouTube as highest-quality MP3s, in parallel.

Each input entry is either a YouTube URL (used as-is) or free text
(resolved to a video via YouTube search). Entries come from CLI arguments
and/or a CSV list file (default: songs.csv next to this script) with the
columns: song, era, genre, status, date, detail. Only `song` is required;
the rest may be blank. The moment a song finishes, its status is written
back to its row: 'downloaded' (with date) or 'failed' (with date and reason
in `detail`) — so the CSV tracks progress live and survives an interrupted
run. Rows already marked 'downloaded' are skipped on later runs — clear the
status cell (or pass --no-archive) to redo them.

    uv run yt/main.py                          # download everything in songs.csv
    uv run yt/main.py "daft punk around the world" -j 2
    uv run yt/main.py --help                   # full flag list + anti-bot playbook
"""

import argparse
import contextlib
import csv
import queue
import shutil
import sys
import threading
from collections import Counter
from datetime import date
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

import yt_dlp
from tqdm import tqdm
from yt_dlp.utils import DownloadCancelled, DownloadError, ExistingVideoReached, parse_bytes

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_LIST = SCRIPT_DIR / "songs.csv"
DEFAULT_OUTPUT = SCRIPT_DIR / "downloads"
CSV_FIELDS = ("song", "era", "genre", "status", "date", "detail")

EPILOG = """\
anti-bot / rate-limit playbook:
  throttling / HTTP 429    built in: 3 workers, jittered 1-3s sleep per download, 0.75s
                           between API requests, retries with backoff. Add --limit-rate 2M
                           to cap bandwidth; don't raise -j above 4.
  "confirm you're not      pass --cookies-from-browser firefox (or chrome, ...) or
   a bot" wall             --cookies cookies.txt exported from a private window you then
                           close; prefer a throwaway account. Residential IP >> VPS/VPN;
                           --ipv4 helps when an IPv6 range is flagged.
  PO tokens / SABR         for heavy use install the PO-token provider plugin into this
                           env: uv add bgutil-ytdlp-pot-provider (auto-discovered by
                           yt-dlp; needs node >= 18).
  JS challenges            yt-dlp needs an external JS runtime (deno recommended, node
                           works). Auto-detected; override with --js-runtime NAME[:PATH].
  extractor breakage       YouTube changes weekly. If downloads suddenly fail en masse:
                           uv lock --upgrade-package yt-dlp && uv sync

quality note: YouTube serves music at ~130-160 kbps Opus at best. The MP3 V0 output
(~200-260 kbps VBR) is the best possible transcode of that source, not added quality.
"""

JS_RUNTIME_CANDIDATES = (("deno", "deno"), ("node", "node"), ("bun", "bun"), ("quickjs", "qjs"))


@dataclass
class Result:
    entry: str
    url: str | None = None
    title: str | None = None
    status: str = "pending"  # done | skipped | failed | cancelled
    detail: str = ""


class TqdmLogger:
    """yt-dlp logger that routes everything through tqdm.write so bars survive."""

    def __init__(self, verbose: bool):
        self.verbose = verbose

    def debug(self, msg):
        if self.verbose:
            tqdm.write(msg)

    info = debug

    def warning(self, msg):
        if self.verbose:
            tqdm.write(f"WARN: {msg}", file=sys.stderr)

    def error(self, msg):
        tqdm.write(f"ERROR: {str(msg).removeprefix('ERROR: ')}", file=sys.stderr)


def shorten(text: str, width: int = 38) -> str:
    text = text.strip()
    return text if len(text) <= width else text[: width - 1] + "…"


def is_url(entry: str) -> bool:
    return urlparse(entry).scheme in ("http", "https")


def parse_args() -> tuple[argparse.ArgumentParser, argparse.Namespace]:
    parser = argparse.ArgumentParser(
        description=__doc__.splitlines()[0],
        epilog=EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("entries", nargs="*", metavar="SONG",
                        help="YouTube URL or search text (added to the list file's entries)")
    parser.add_argument("-f", "--file", type=Path, metavar="PATH",
                        help="song list CSV with a 'song' column; status/date/detail are "
                             "written back to each row the moment it finishes "
                             f"(default: {DEFAULT_LIST} if present)")
    parser.add_argument("-o", "--output-dir", type=Path, default=DEFAULT_OUTPUT, metavar="DIR",
                        help="where the .mp3 files go (default: %(default)s)")
    parser.add_argument("-j", "--jobs", type=int, default=3, metavar="N",
                        help="parallel downloads (default: %(default)s; keep <= 4 to stay polite)")
    parser.add_argument("--sleep", type=float, default=1.0, metavar="SEC",
                        help="min sleep before each download (default: %(default)s)")
    parser.add_argument("--max-sleep", type=float, default=3.0, metavar="SEC",
                        help="max sleep before each download; jitter range with --sleep (default: %(default)s)")
    parser.add_argument("--limit-rate", metavar="RATE",
                        help="per-download bandwidth cap, e.g. 500K or 2M")
    cookies = parser.add_mutually_exclusive_group()
    cookies.add_argument("--cookies", type=Path, metavar="FILE",
                         help="Netscape cookies.txt for an authenticated session")
    cookies.add_argument("--cookies-from-browser", metavar="BROWSER[:PROFILE]",
                         help="read cookies straight from a browser, e.g. firefox or chrome:Default")
    parser.add_argument("--proxy", metavar="URL", help="HTTP/HTTPS/SOCKS proxy")
    parser.add_argument("--ipv4", action="store_true", help="force IPv4 (some IPv6 ranges are bot-flagged)")
    parser.add_argument("--archive", type=Path, metavar="FILE",
                        help="download archive path (default: <output-dir>/.archive.txt)")
    parser.add_argument("--no-archive", action="store_true",
                        help="disable the download archive and re-process rows already "
                             "marked downloaded (re-download everything)")
    parser.add_argument("--audio-quality", default="0", metavar="Q",
                        help="MP3 quality: LAME VBR preset 0-10 (0 = best) or CBR bitrate like 192 (default: %(default)s)")
    parser.add_argument("--embed-thumbnail", action="store_true",
                        help="embed the video thumbnail as cover art")
    parser.add_argument("--js-runtime", default="auto", metavar="NAME[:PATH]",
                        help="JS runtime for YouTube challenges: deno|node|bun|quickjs, "
                             "optional executable path (default: auto-detect)")
    parser.add_argument("-v", "--verbose", action="store_true", help="show yt-dlp log output")
    args = parser.parse_args()
    if args.limit_rate and parse_bytes(args.limit_rate) is None:
        parser.error(f"--limit-rate: cannot parse {args.limit_rate!r} (try 500K, 2M, ...)")
    return parser, args


def cell(row: dict, key: str) -> str:
    return (row.get(key) or "").strip()


def read_csv_rows(path: Path) -> tuple[list[dict], list[str]]:
    """Read the song list CSV; returns (rows, fieldnames incl. any extras)."""
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or "song" not in reader.fieldnames:
            sys.exit(f"{path}: expected a CSV header with a 'song' column, e.g.: "
                     + ",".join(CSV_FIELDS))
        rows = list(reader)
    fields = list(reader.fieldnames) + [c for c in CSV_FIELDS if c not in reader.fieldnames]
    return rows, fields


def read_entries(args: argparse.Namespace) -> tuple[list[str], Path | None]:
    entries = list(args.entries)
    list_file = args.file if args.file else (DEFAULT_LIST if DEFAULT_LIST.exists() else None)
    if list_file:
        rows, _ = read_csv_rows(Path(list_file))
        done = 0
        for row in rows:
            song = cell(row, "song")
            if not song:
                continue
            if cell(row, "status").lower() == "downloaded" and not args.no_archive:
                done += 1
                continue
            entries.append(song)
        if done:
            print(f"skipping {done} row(s) already marked downloaded "
                  "(clear the status cell or pass --no-archive to redo)")
    return list(dict.fromkeys(entries)), list_file


def update_list_file(path: Path, results: list[Result]) -> int:
    """Write download status/date/detail back onto the matching CSV rows."""
    by_entry = {r.entry: r for r in results}
    today = date.today().isoformat()
    rows, fields = read_csv_rows(path)
    changed = 0
    for row in rows:
        res = by_entry.get(cell(row, "song"))
        if res is None or res.status == "cancelled":
            continue
        old = dict(row)
        if res.status in ("done", "skipped"):
            # keep the original download date on archive-skipped re-runs
            keep_date = (res.status == "skipped" and cell(row, "date")
                         and cell(row, "status").lower() == "downloaded")
            row["status"] = "downloaded"
            row["date"] = row["date"] if keep_date else today
            row["detail"] = ""
        else:  # failed
            row["status"], row["date"] = "failed", today
            row["detail"] = res.detail[:100]
        changed += row != old
    tmp = path.with_name(path.name + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, restval="", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    tmp.replace(path)  # atomic: a crash mid-write can't leave a torn CSV
    return changed


def write_status(path: Path | None, batch: list[Result]) -> int:
    """Push statuses to the CSV right away; tracking failures never kill the batch."""
    batch = [r for r in batch if r.status != "cancelled"]
    if path is None or not batch:
        return 0
    try:
        return update_list_file(path, batch)
    except (Exception, SystemExit) as e:  # SystemExit: read_csv_rows exits on a bad header
        tqdm.write(f"WARN: could not update {path}: {e}", file=sys.stderr)
        return 0


def resolve_js_runtime(spec: str) -> tuple[str, dict] | None:
    if spec != "auto":
        name, _, path = spec.partition(":")
        name = name.lower()
        if name not in {n for n, _ in JS_RUNTIME_CANDIDATES}:
            sys.exit(f"unsupported --js-runtime {name!r} (use deno, node, bun or quickjs)")
        return name, ({"path": path} if path else {})
    for name, exe in JS_RUNTIME_CANDIDATES:
        found = shutil.which(exe)
        if found:
            return name, ({} if exe == name else {"path": found})
    return None


def preflight(args: argparse.Namespace) -> None:
    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg not found on PATH — it is required for MP3 extraction")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    if args.archive is None:
        args.archive = args.output_dir / ".archive.txt"
    args.js_runtime_resolved = resolve_js_runtime(args.js_runtime)
    if args.js_runtime_resolved is None:
        print("warning: no JavaScript runtime found (deno/node/bun/quickjs).\n"
              "  YouTube JS challenges cannot be solved -> throttled or missing formats.\n"
              "  Install deno, or point at one with --js-runtime node:/path/to/node",
              file=sys.stderr)


def build_base_opts(args: argparse.Namespace) -> dict:
    opts = {
        # tqdm owns the terminal; yt-dlp messages go through TqdmLogger
        "quiet": True,
        "noprogress": True,
        "logger": TqdmLogger(args.verbose),
        # network & politeness
        "socket_timeout": 20,
        "retries": 10,
        "extractor_retries": 3,
        "sleep_interval_requests": 0.75,
        "noplaylist": True,
    }
    if args.js_runtime_resolved:
        name, cfg = args.js_runtime_resolved
        opts["js_runtimes"] = {name: cfg}
    if args.ipv4:
        opts["source_address"] = "0.0.0.0"
    if args.proxy:
        opts["proxy"] = args.proxy
    if args.cookies:
        opts["cookiefile"] = str(args.cookies)
    elif args.cookies_from_browser:
        browser, _, profile = args.cookies_from_browser.partition(":")
        opts["cookiesfrombrowser"] = (browser, profile or None, None, None)
    return opts


def resolve_search(entry: str, base_opts: dict) -> tuple[str, str]:
    """Turn free text into (watch URL, title) via a single flat search request."""
    opts = {**base_opts, "skip_download": True, "extract_flat": True, "playlist_items": "1"}
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(f"ytsearch1:{entry}", download=False)
    hits = (info or {}).get("entries") or []
    if not hits:
        raise DownloadError(f"no YouTube search result for {entry!r}")
    hit = hits[0]
    url = hit.get("url") or f"https://www.youtube.com/watch?v={hit['id']}"
    return url, hit.get("title") or entry


def make_progress_hook(bar: tqdm, stop_event: threading.Event):
    def hook(d: dict) -> None:
        if stop_event.is_set():
            raise DownloadCancelled("interrupted by user")
        if d["status"] == "downloading":
            total = d.get("total_bytes") or d.get("total_bytes_estimate")
            n = d.get("downloaded_bytes") or 0
            if n < bar.n:  # a new file/fragment started
                bar.reset(total=total)
            elif total and bar.total != total:
                bar.total = total
            title = (d.get("info_dict") or {}).get("title")
            # disabled (non-TTY) bars have no .desc attribute until one is set
            if title and getattr(bar, "desc", None) != shorten(title):
                bar.set_description_str(shorten(title), refresh=False)
            bar.n = n
            bar.refresh()
        elif d["status"] == "finished":
            if bar.total:
                bar.n = bar.total
            bar.set_postfix_str("ffmpeg -> mp3", refresh=True)
    return hook


def make_pp_hook(bar: tqdm):
    def hook(d: dict) -> None:
        if d.get("status") == "started":
            bar.set_postfix_str(d.get("postprocessor") or "postprocess", refresh=True)
        elif d.get("status") == "finished" and d.get("postprocessor") == "MoveFiles":
            bar.set_postfix_str("done", refresh=True)
    return hook


def build_download_opts(args: argparse.Namespace, base_opts: dict,
                        bar: tqdm, stop_event: threading.Event) -> dict:
    postprocessors = [
        {"key": "FFmpegExtractAudio", "preferredcodec": "mp3",
         "preferredquality": args.audio_quality},
        {"key": "FFmpegMetadata", "add_metadata": True},
    ]
    opts = {
        **base_opts,
        "format": "bestaudio/best",
        "paths": {"home": str(args.output_dir)},
        "outtmpl": {"default": "%(title)s [%(id)s].%(ext)s"},
        "postprocessors": postprocessors,
        "overwrites": False,
        "continuedl": True,
        "sleep_interval": args.sleep,
        "max_sleep_interval": max(args.sleep, args.max_sleep),
        "fragment_retries": 10,
        "concurrent_fragment_downloads": 1,  # politeness: -j controls parallelism, not per-file
        "ignoreerrors": False,  # per-song failures are handled in process_entry
        "progress_hooks": [make_progress_hook(bar, stop_event)],
        "postprocessor_hooks": [make_pp_hook(bar)],
    }
    if args.embed_thumbnail:
        opts["writethumbnail"] = True
        postprocessors.insert(0, {"key": "FFmpegThumbnailsConvertor", "format": "jpg",
                                  "when": "before_dl"})
        postprocessors.append({"key": "EmbedThumbnail", "already_have_thumbnail": False})
    if not args.no_archive:
        opts["download_archive"] = str(args.archive)
        opts["break_on_existing"] = True
    if args.limit_rate:
        opts["ratelimit"] = parse_bytes(args.limit_rate)
    return opts


def final_filepath(info: dict | None) -> str:
    if not info:
        return ""
    for req in info.get("requested_downloads") or []:
        if req.get("filepath"):
            return req["filepath"]
    return info.get("filepath") or ""


def process_entry(entry: str, args: argparse.Namespace, base_opts: dict,
                  slots: "queue.Queue[int]", stop_event: threading.Event) -> Result:
    res = Result(entry=entry)
    if stop_event.is_set():
        res.status = "cancelled"
        return res
    slot = slots.get()
    bar = tqdm(total=None, unit="B", unit_scale=True, unit_divisor=1024,
               position=slot, leave=False, dynamic_ncols=True, disable=None,
               desc=shorten(entry))
    try:
        if is_url(entry):
            res.url = entry
        else:
            res.url, res.title = resolve_search(entry, base_opts)
            bar.set_description_str(shorten(res.title))
        # fresh YoutubeDL per task: the class is not thread-safe for concurrent reuse
        dl_opts = build_download_opts(args, base_opts, bar, stop_event)
        with yt_dlp.YoutubeDL(dl_opts) as ydl:
            info = ydl.extract_info(res.url, download=True)
        res.title = res.title or (info or {}).get("title")
        res.status, res.detail = "done", final_filepath(info)
    except ExistingVideoReached:  # must precede DownloadCancelled (its parent class)
        res.status, res.detail = "skipped", "already in archive"
    except DownloadCancelled:
        res.status = "cancelled"
    except DownloadError as e:
        msg = str(e).splitlines()[0] if str(e) else type(e).__name__
        res.status, res.detail = "failed", msg.removeprefix("ERROR: ")[:200]
    except Exception as e:  # never let one song take down the batch
        res.status, res.detail = "failed", f"{type(e).__name__}: {e}"
    finally:
        bar.close()
        slots.put(slot)
    return res


def print_summary(results: list[Result], interrupted: bool) -> None:
    order = {"done": 0, "skipped": 1, "cancelled": 2, "failed": 3}
    mark = {"done": "+", "skipped": ">", "cancelled": "~", "failed": "!"}
    print("\n" + "=" * 72)
    for r in sorted(results, key=lambda r: order.get(r.status, 9)):
        line = f"{mark.get(r.status, '?')} {r.status:<9} {r.title or r.entry}"
        if r.detail:
            line += f"  ({r.detail})"
        print(line)
    counts = Counter(r.status for r in results)
    print("-" * 72)
    tally = ", ".join(f"{n} {status}" for status, n in counts.items())
    print(tally + (" — interrupted" if interrupted else ""))
    if counts.get("failed", 0) >= 2:
        print("hint: widespread failures usually mean yt-dlp needs an update:\n"
              "      uv lock --upgrade-package yt-dlp && uv sync")


def main() -> int:
    parser, args = parse_args()
    entries, list_file = read_entries(args)
    if not entries:
        parser.error(f"no songs given — pass entries as arguments or create {DEFAULT_LIST}")
    preflight(args)
    base_opts = build_base_opts(args)

    workers = max(1, min(args.jobs, len(entries)))
    slots: queue.Queue[int] = queue.Queue()
    for i in range(1, workers + 1):
        slots.put(i)
    stop_event = threading.Event()
    results: list[Result] = []
    collected: set = set()
    interrupted = False
    list_path = Path(list_file) if list_file else None
    csv_updates = 0

    overall = tqdm(total=len(entries), desc="Songs", unit="song",
                   position=0, leave=True, dynamic_ncols=True, disable=None)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(process_entry, e, args, base_opts, slots, stop_event): e
                   for e in entries}
        try:
            for fut in as_completed(futures):
                res = fut.result()
                results.append(res)
                collected.add(fut)
                csv_updates += write_status(list_path, [res])
                overall.update(1)
        except KeyboardInterrupt:
            interrupted = True
            stop_event.set()
            tqdm.write("interrupted — cancelling queued songs, aborting in-flight downloads…")
            pool.shutdown(wait=True, cancel_futures=True)
            for fut, entry in futures.items():
                if fut in collected:
                    continue
                if fut.cancelled():
                    results.append(Result(entry=entry, status="cancelled", detail="not started"))
                elif fut.done():
                    with contextlib.suppress(Exception):
                        results.append(fut.result())
    overall.close()

    print_summary(results, interrupted)
    if list_path and results:
        # catch-all pass: covers interrupt stragglers and any per-song write that failed
        csv_updates += write_status(list_path, results)
        print(f"updated {csv_updates} row status(es) in {list_file}")
    if interrupted:
        return 130
    return 1 if any(r.status == "failed" for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
