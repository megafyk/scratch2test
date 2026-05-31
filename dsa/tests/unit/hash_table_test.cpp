#include "test_utils.hpp"

#include "dsa/data_structures/hash_tables/hash_table.hpp"

#include <cstddef>
#include <string>

using dsa::data_structures::hash_tables::HashTable;

namespace
{
void test_empty()
{
    HashTable<int, int> t;
    CHECK_EQ(t.size(), 0u);
    CHECK(t.empty());
    CHECK(t.find(42) == nullptr);
    CHECK(!t.contains(42));
    CHECK(!t.erase(42)); // erasing from an empty table reports nothing removed
}

void test_insert_and_find()
{
    HashTable<int, int> t;
    t.insert(1, 10);
    t.insert(2, 20);
    t.insert(3, 30);

    CHECK_EQ(t.size(), 3u);
    CHECK(!t.empty());
    CHECK(t.contains(2));

    int *v = t.find(2);
    CHECK(v != nullptr);
    if (v != nullptr)
        CHECK_EQ(*v, 20);

    CHECK(t.find(99) == nullptr);
    CHECK(!t.contains(99));
}

void test_overwrite_duplicate_key()
{
    HashTable<int, int> t;
    t.insert(7, 1);
    t.insert(7, 2);
    t.insert(7, 3);

    CHECK_EQ(t.size(), 1u); // a repeated key must not grow the table
    int *v = t.find(7);
    CHECK(v != nullptr);
    if (v != nullptr)
        CHECK_EQ(*v, 3); // the most recent value wins
}

void test_erase()
{
    HashTable<int, int> t;
    t.insert(1, 100);
    t.insert(2, 200);

    CHECK(t.erase(1));
    CHECK(!t.contains(1));
    CHECK(t.find(1) == nullptr);
    CHECK_EQ(t.size(), 1u);

    CHECK(!t.erase(1));   // already removed
    CHECK(!t.erase(999)); // never present
    CHECK_EQ(t.size(), 1u);
}

void test_grow_and_collisions()
{
    HashTable<int, int> t;
    const int n = 1000;
    for (int i = 0; i < n; ++i)
        t.insert(i, i * i);

    CHECK_EQ(t.size(), static_cast<std::size_t>(n));

    bool all_found = true;
    for (int i = 0; i < n; ++i)
    {
        int *v = t.find(i);
        if (v == nullptr || *v != i * i)
            all_found = false;
    }
    CHECK(all_found); // every entry must survive rehashing
}

void test_string_keys()
{
    HashTable<std::string, int> t;
    t.insert("alpha", 1);
    t.insert("beta", 2);

    CHECK(t.contains("alpha"));
    int *v = t.find("beta");
    CHECK(v != nullptr);
    if (v != nullptr)
        CHECK_EQ(*v, 2);
    CHECK(!t.contains("gamma"));
}
} // namespace

int main()
{
    test_empty();
    test_insert_and_find();
    test_overwrite_duplicate_key();
    test_erase();
    test_grow_and_collisions();
    test_string_keys();

    return dsa::test::summary("hash_table");
}
