// Copy-template for a unit test. Steps:
//   1. Copy to tests/unit/<name>_test.cpp
//   2. Fix the include path and the using-declaration below.
//   3. Register it in tests/CMakeLists.txt:  dsa_add_unit_test(<name>_test)
// Uncomment each assertion as you implement the matching behavior.
#include "test_utils.hpp"

#include "dsa/data_structures/your_category/your_structure.hpp"

// using dsa::data_structures::your_category::YourStructure;

namespace
{
void test_starts_empty()
{
    // YourStructure<int> s;
    // CHECK(s.empty());
    // CHECK_EQ(s.size(), 0u);
}

// TODO: add one focused test function per behavior, then call it from main().
} // namespace

int main()
{
    test_starts_empty();
    return dsa::test::summary("your_structure");
}
