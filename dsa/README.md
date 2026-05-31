# C++ DSA Workshop

A scaffold for implementing data structures and algorithms **from scratch in C++**,
for learning. Interfaces are provided as stubs; you write the bodies, guided by unit
tests and checked by sanitizers.

> Status: interface stubs only. `mvector` and `hash_table` declare their interfaces;
> the method bodies are yours to implement. See [docs/ROADMAP.md](docs/ROADMAP.md).

## Build & test

Requires CMake >= 3.20 and a C++20 compiler (GCC or Clang). The default build type is
`Debug`, with AddressSanitizer + UBSan enabled for tests.

```bash
cmake -S . -B build
cmake --build build
ctest --test-dir build --output-on-failure
```

Until you implement a structure's bodies, its test fails to **link** (undefined
references) — that is the expected starting point of the red→green loop.

Options:

- `-DDSA_ENABLE_SANITIZERS=OFF` — turn off ASan/UBSan.
- `-DDSA_BUILD_EXAMPLES=ON` — build `examples/`.
- `-DDSA_BUILD_BENCHMARKS=ON` — build `benchmarks/`.

## The learning loop

1. Copy `templates/data_structure.hpp` → `include/dsa/data_structures/<category>/<name>.hpp`.
2. Copy `templates/unit_test.cpp` → `tests/unit/<name>_test.cpp`, then add
   `dsa_add_unit_test(<name>_test)` to `tests/CMakeLists.txt`.
3. Write the test first, then implement until `ctest` is green under sanitizers.
4. Annotate each method with its Big-O.

See [docs/ROADMAP.md](docs/ROADMAP.md) for the checklist and
[docs/structure.md](docs/structure.md) for the layout.

## Layout

```text
dsa/
├── CMakeLists.txt          # dsa (header-only lib) + warning/sanitizer helpers
├── include/dsa/            # the library you implement (headers only)
│   └── data_structures/
│       ├── arrays/mvector.hpp
│       └── hash_tables/hash_table.hpp
├── tests/
│   ├── test_utils.hpp      # tiny zero-dependency CHECK/CHECK_EQ harness
│   └── unit/               # one <name>_test.cpp per structure
├── templates/              # copy-templates for a new structure + its test
├── examples/               # optional manual demos (-DDSA_BUILD_EXAMPLES=ON)
├── benchmarks/             # optional perf checks (-DDSA_BUILD_BENCHMARKS=ON)
└── docs/                   # ROADMAP.md, structure.md
```
