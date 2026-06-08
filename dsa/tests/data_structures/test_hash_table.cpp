
// tests/data_structures/test_hash_table.cpp
#include "data_structures/hash_table.h"
#include <cstddef>
#include <gtest/gtest.h>

TEST(HashTable, constructor) {
    int universal = 7;
    dsa::HashTable<int, int> hashTable(universal);
<<<<<<< HEAD
    EXPECT_EQ(universal, hashTable.bucket().size());
    EXPECT_EQ(universal, hashTable.size());
=======
    EXPECT_EQ(universal, hashTable.getData().size());
    EXPECT_EQ(universal, hashTable.getSize());
>>>>>>> 93152b4c999078c3e28cef15af74d024ddd742c3
}

TEST(HashTable, add) {
    int universal = 7;
    dsa::HashTable<int, std::string> hashTable(universal);
    hashTable.add(1, "red");
<<<<<<< HEAD
    EXPECT_EQ(1, hashTable.bucket()[1].value().key);
    EXPECT_EQ("red", hashTable.bucket()[1].value().val);
=======
    EXPECT_EQ(1, hashTable.getData()[1].key == 1);
    EXPECT_EQ("red", hashTable.getData()[1].val == "red");
>>>>>>> 93152b4c999078c3e28cef15af74d024ddd742c3
}
