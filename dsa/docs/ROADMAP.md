# Roadmap

A checklist of structures and algorithms to build from scratch. Tick each off once
it is implemented with a passing unit test. The order is a suggestion, not a rule.

## Workflow: adding a structure

1. Copy `templates/data_structure.hpp` to
   `include/dsa/data_structures/<category>/<name>.hpp`; rename the namespace and class.
2. Copy `templates/unit_test.cpp` to `tests/unit/<name>_test.cpp`; fix the include and
   register it in `tests/CMakeLists.txt` with `dsa_add_unit_test(<name>_test)`.
3. Write or extend the test first (red), then implement until it passes (green).
4. Build and run under sanitizers: `cmake --build build && ctest --test-dir build`.
5. Record each method's Big-O in a comment.

## Data structures

- [ ] Dynamic array — `data_structures/arrays/mvector.hpp` _(stub ready)_
- [ ] Hash table (separate chaining) — `data_structures/hash_tables/hash_table.hpp` _(stub ready)_
- [ ] Singly / doubly linked list — `linked_lists/`
- [ ] Stack — `stacks/`
- [ ] Queue / deque — `queues/`
- [ ] Heap / priority queue — `heaps/`
- [ ] Binary search tree / balanced tree — `trees/`
- [ ] Graph (adjacency list) — `graphs/`
- [ ] Trie — `tries/`
- [ ] Disjoint set (union-find) — `disjoint_sets/`

## Algorithms

- [ ] Sorting (insertion, merge, quick, heap) — `algorithms/sorting/`
- [ ] Searching (binary search and variants) — `algorithms/searching/`
- [ ] Graph traversal (BFS, DFS, shortest paths) — `algorithms/graph/`
- [ ] Dynamic programming — `algorithms/dynamic_programming/`
- [ ] Greedy — `algorithms/greedy/`
- [ ] Backtracking — `algorithms/backtracking/`
- [ ] String algorithms — `algorithms/string/`
- [ ] Math / number theory — `algorithms/math/`

`mvector` and `hash_table` are interface stubs: the declarations exist, but the method
bodies are yours to write. Check them off once implemented and green.
