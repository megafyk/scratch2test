# Structure Guide

## Public Headers

- `include/dsa/data_structures/`: public interfaces for custom containers and supporting nodes.
- `include/dsa/algorithms/`: public interfaces for algorithm families.
- `include/dsa/common/`: shared types, utilities, and helpers.

## Source Layout

- `src/data_structures/`: implementations that mirror the public header hierarchy.
- `src/algorithms/`: implementations that mirror the public header hierarchy.
- `src/common/`: shared internal utilities.

## Categories

### Data Structures

- `arrays/`
- `linked_lists/`
- `stacks/`
- `queues/`
- `hash_tables/`
- `heaps/`
- `trees/`
- `graphs/`
- `tries/`
- `disjoint_sets/`

### Algorithms

- `sorting/`
- `searching/`
- `graph/`
- `dynamic_programming/`
- `greedy/`
- `backtracking/`
- `string/`
- `math/`

## Validation and Tooling

- `tests/unit/`: small focused correctness tests.
- `tests/integration/`: larger end-to-end scenarios.
- `benchmarks/`: performance comparisons and profiling harnesses.
- `examples/`: quick manual demos and usage notes.
- `cmake/`: reusable CMake modules if the project grows.
