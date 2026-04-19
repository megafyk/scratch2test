# C++ DSA Skeleton

Project structure for building data structures and algorithms from scratch in C++.

This scaffold intentionally contains no implementations yet. It provides a clean layout
for headers, sources, tests, benchmarks, examples, and docs.

## Suggested Workflow

1. Add public interfaces under `include/dsa/...`.
2. Add implementations under `src/...`.
3. Add validation under `tests/...`.
4. Keep experiments in `examples/` and performance checks in `benchmarks/`.

## Build

```bash
cmake -S . -B build
cmake --build build
```

Optional targets:

- `-DDSA_BUILD_TESTS=ON`
- `-DDSA_BUILD_BENCHMARKS=ON`
- `-DDSA_BUILD_EXAMPLES=ON`

## Layout

```text
dsa/
├── CMakeLists.txt
├── README.md
├── benchmarks/
├── cmake/
├── docs/
├── examples/
├── include/
│   └── dsa/
│       ├── algorithms/
│       ├── common/
│       └── data_structures/
├── src/
│   ├── algorithms/
│   ├── common/
│   └── data_structures/
└── tests/
    ├── integration/
    └── unit/
```

See `docs/structure.md` for the category breakdown.
