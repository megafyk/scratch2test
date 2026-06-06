# DSA - Data Structures & Algorithms

Learning project implementing data structures and algorithms from scratch in C++20.

## Tech Stack

- C++20
- CMake
- Google Test (gtest)

## Project Structure

```
dsa/
├── include/
│   ├── data_structures/   # Header-only data structure implementations
│   └── algorithms/        # Header-only algorithm implementations
├── tests/
│   ├── data_structures/   # Tests for data structures
│   └── algorithms/        # Tests for algorithms
├── build/                 # Build output (git-ignored)
│   ├── bin/               # Test executables
│   └── lib/               # Static libraries
├── CMakeLists.txt
└── README.md
```

All code uses the `dsa::` namespace.

## Build

```bash
cmake -B build
cmake --build build
```

To clean and rebuild:

```bash
rm -rf build
cmake -B build
cmake --build build
```

## Run Tests

```bash
ctest --test-dir build --output-on-failure
```

## How to Add a New Implementation

### 1. Copy template and create header in `include/`

```bash
cp include/data_structures/.template.h include/data_structures/linked_list.h
```

```cpp
// include/data_structures/linked_list.h
#pragma once

namespace dsa {

template <typename T>
class LinkedList {
    // your implementation
};

} // namespace dsa
```

### 2. Copy template and create test in `tests/`

```bash
cp tests/data_structures/.template.cpp tests/data_structures/test_linked_list.cpp
```

```cpp
// tests/data_structures/test_linked_list.cpp
#include <gtest/gtest.h>
#include "data_structures/linked_list.h"

using namespace dsa;

TEST(LinkedList, PushFront) {
    LinkedList<int> list;
    list.push_front(1);
    EXPECT_EQ(list.front(), 1);
}
```

### 3. Register test in `tests/CMakeLists.txt`

```cmake
add_executable(test_linked_list data_structures/test_linked_list.cpp)
target_include_directories(test_linked_list PRIVATE ${PROJECT_SOURCE_DIR}/include)
target_link_libraries(test_linked_list GTest::gtest_main)
gtest_discover_tests(test_linked_list)
```

### 4. Build & test

```bash
cmake --build build && ctest --test-dir build --output-on-failure
```

## Adding Libraries

Add via `FetchContent` in root `CMakeLists.txt`:

```cmake
FetchContent_Declare(
  fmt
  GIT_REPOSITORY https://github.com/fmtlib/fmt.git
  GIT_TAG 10.2.1
)
FetchContent_MakeAvailable(fmt)
```

Then link where needed:

```cmake
target_link_libraries(test_something GTest::gtest_main fmt::fmt)
```
