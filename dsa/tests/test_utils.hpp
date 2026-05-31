#pragma once
// Minimal, zero-dependency test harness for the dsa project.
//
// Usage:
//   #include "test_utils.hpp"
//   void test_thing() { CHECK(1 + 1 == 2); CHECK_EQ(value, 3); }
//   int main() { test_thing(); return dsa::test::summary("thing"); }
//
// Every function is `inline` so this header can be included in any number of
// translation units without breaking the One Definition Rule.
#include <cstddef>
#include <iostream>

namespace dsa::test
{
// Single program-wide failure counter (one definition thanks to the inline
// function-local static).
inline int &failure_count()
{
    static int count = 0;
    return count;
}

inline void check(bool ok, const char *expr, const char *file, int line)
{
    if (!ok)
    {
        ++failure_count();
        std::cerr << "FAIL: " << expr << " (" << file << ':' << line << ")\n";
    }
}

template <typename A, typename B>
inline void check_eq(const A &a, const B &b, const char *expr, const char *file, int line)
{
    if (!(a == b))
    {
        ++failure_count();
        std::cerr << "FAIL: " << expr << " (" << file << ':' << line << ")\n"
                  << "        left  = " << a << "\n"
                  << "        right = " << b << '\n';
    }
}

// Print a summary and return a process exit code (0 = success, 1 = failures).
// Call from the end of main(): `return dsa::test::summary("my_suite");`
inline int summary(const char *suite)
{
    if (failure_count() == 0)
    {
        std::cout << "[PASS] " << suite << ": all checks passed\n";
        return 0;
    }
    std::cerr << "[FAIL] " << suite << ": " << failure_count() << " check(s) failed\n";
    return 1;
}
} // namespace dsa::test

// CHECK(cond): assert a boolean condition.
// CHECK_EQ(a, b): assert a == b and print both sides on failure (needs operator<<).
#define CHECK(cond) ::dsa::test::check((cond), #cond, __FILE__, __LINE__)
#define CHECK_EQ(a, b) ::dsa::test::check_eq((a), (b), #a " == " #b, __FILE__, __LINE__)
