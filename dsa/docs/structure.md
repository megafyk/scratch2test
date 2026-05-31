# Structure Guide

## Library (header-only)

Everything is templates, so the `dsa` library is header-only — there is no `src/`.
Implement method bodies inline in the header (required for templates).

- `include/dsa/data_structures/<category>/<name>.hpp`: one structure per header, in
  namespace `dsa::data_structures::<category>`.
- `include/dsa/algorithms/<family>/...`: algorithm families (add when you start them).

Currently present (as stubs):

- `data_structures/arrays/mvector.hpp`
- `data_structures/hash_tables/hash_table.hpp`

Folders for the other categories are created on demand: copy a template and make the
directory when you start that topic. See [ROADMAP.md](ROADMAP.md) for the full list.

## Tests

- `tests/test_utils.hpp`: zero-dependency harness — `CHECK`, `CHECK_EQ`, and
  `dsa::test::summary()`.
- `tests/unit/<name>_test.cpp`: one focused suite per structure, registered with
  `dsa_add_unit_test(<name>_test)` in `tests/CMakeLists.txt`.
- Tests compile with `-Wall -Wextra -Wpedantic` and, by default, ASan + UBSan.

## Templates

- `templates/data_structure.hpp` and `templates/unit_test.cpp`: copy-ready scaffolds
  for adding a new structure and its test. Not part of the build.

## Other

- `examples/`: optional manual demos (`-DDSA_BUILD_EXAMPLES=ON`).
- `benchmarks/`: optional performance checks (`-DDSA_BUILD_BENCHMARKS=ON`).
