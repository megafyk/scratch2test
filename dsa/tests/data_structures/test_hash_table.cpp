
// tests/data_structures/test_hash_table.cpp
#include "data_structures/hash_table.h"
#include <cstddef>
#include <gtest/gtest.h>

TEST(HashTable, constructor) {
    int universal = 7;
    dsa::HashTable<int, int> hashTable(universal);
    EXPECT_EQ(universal, hashTable.bucket().size());
    EXPECT_EQ(universal, hashTable.size());
}

TEST(HashTable, add) {
    int universal = 7;
    dsa::HashTable<int, std::string> hashTable(universal);
    hashTable.add(1, "red");
    EXPECT_EQ(1, hashTable.bucket()[1].value().key);
    EXPECT_EQ("red", hashTable.bucket()[1].value().val);
}
