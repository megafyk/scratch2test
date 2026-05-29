cmake_minimum_required(VERSION 3.20)

project(
    dsa
    VERSION 0.1.0
    DESCRIPTION "Data structures and algorithms implemented from scratch in C++"
    LANGUAGES CXX
)

# Learning project: default to a Debug build (debug info + sanitizers) unless the
# user picked a build type, or a multi-config generator (e.g. Ninja Multi-Config)
# is in use.
if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
    set(CMAKE_BUILD_TYPE Debug CACHE STRING "Build type" FORCE)
endif()

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

option(DSA_BUILD_TESTS "Build the test suite" ON)
option(DSA_BUILD_BENCHMARKS "Build benchmarks" OFF)
option(DSA_BUILD_EXAMPLES "Build example programs" OFF)
option(DSA_ENABLE_SANITIZERS "Build tests/examples with AddressSanitizer + UBSan" ON)

# ---------------------------------------------------------------------------
# dsa: the library you implement. Everything is templates living in include/,
# so this is a header-only INTERFACE target with no compiled sources.
# (If you later add a non-template .cpp, create a STATIC library here instead.)
# ---------------------------------------------------------------------------
add_library(dsa INTERFACE)
add_library(dsa::dsa ALIAS dsa)
target_include_directories(dsa INTERFACE ${PROJECT_SOURCE_DIR}/include)
target_compile_features(dsa INTERFACE cxx_std_20)

# ---------------------------------------------------------------------------
# Dev-only helpers, linked by tests & examples but never by `dsa` itself so a
# consumer of the library is never forced into these flags.
# ---------------------------------------------------------------------------
add_library(dsa_warnings INTERFACE)
target_compile_options(
    dsa_warnings
    INTERFACE
        $<$<CXX_COMPILER_ID:GNU,Clang,AppleClang>:-Wall;-Wextra;-Wpedantic>
)

# Always defined (empty when disabled) so targets can link it unconditionally.
add_library(dsa_sanitizers INTERFACE)
if(DSA_ENABLE_SANITIZERS AND CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
    target_compile_options(
        dsa_sanitizers
        INTERFACE -fsanitize=address,undefined -fno-omit-frame-pointer
    )
    target_link_options(dsa_sanitizers INTERFACE -fsanitize=address,undefined)
endif()

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
