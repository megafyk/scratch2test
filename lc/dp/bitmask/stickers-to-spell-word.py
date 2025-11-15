class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        sticker_cnt = [Counter(sticker) for sticker in stickers]
        INF = sys.maxsize
        @cache
        def dp(mask):
            if mask == (1 << len(target)) - 1:
                return 0
            res = INF

            for cnt in sticker_cnt:
                nw_sticker = cnt.copy()
                nw_mask = mask
                for idx, c in enumerate(target):
                    if (nw_mask >> idx) & 1 == 0 and nw_sticker[c] > 0:
                        nw_sticker[c] -= 1
                        nw_mask |= (1 << idx)

                if nw_mask != mask:
                    res = min(res, dp(nw_mask) + 1)

            return res
        res = dp(0)
        return -1 if res == INF else res
