cmake_minimum_required(VERSION 3.20)

project(
    dsa
    VERSION 0.1.0
    DESCRIPTION "Data structures and algorithms implemented from scratch in C++"
    LANGUAGES CXX
)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

option(DSA_BUILD_TESTS "Build the test suite" ON)
option(DSA_BUILD_BENCHMARKS "Build benchmarks" OFF)
option(DSA_BUILD_EXAMPLES "Build example programs" OFF)

add_subdirectory(src)

include(CTest)

if(DSA_BUILD_TESTS AND BUILD_TESTING)
    add_subdirectory(tests)
endif()

if(DSA_BUILD_BENCHMARKS)
    add_subdirectory(benchmarks)
endif()

if(DSA_BUILD_EXAMPLES)
    add_subdirectory(examples)
endif()
