
// tests/data_structures/test_hash_table.cpp
#include "data_structures/hash_table.h"
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

TEST(HashTable, add_twice) {
    int universal = 7;
    dsa::HashTable<int, std::string> hashTable(universal);
    hashTable.add(1, "red");
    hashTable.add(2, "green");
    EXPECT_EQ(1, hashTable.bucket()[1].value().key);
    EXPECT_EQ("red", hashTable.bucket()[1].value().val);
    EXPECT_EQ(2, hashTable.bucket()[2].value().key);
    EXPECT_EQ("green", hashTable.bucket()[2].value().val);
}

TEST(HashTable, add_dup) {
    int universal = 7;
    dsa::HashTable<int, std::string> hashTable(universal);
    hashTable.add(1, "red");
    hashTable.add(2, "green");
    hashTable.add(8, "blue");
    hashTable.add(7, "yellow");
    EXPECT_EQ(1, hashTable.bucket()[1].value().key);
    EXPECT_EQ("red", hashTable.bucket()[1].value().val);
    EXPECT_EQ(2, hashTable.bucket()[2].value().key);
    EXPECT_EQ("green", hashTable.bucket()[2].value().val);
    EXPECT_EQ(8, hashTable.bucket()[3].value().key);
    EXPECT_EQ("blue", hashTable.bucket()[3].value().val);
    EXPECT_EQ(7, hashTable.bucket()[0].value().key);
    EXPECT_EQ("yellow", hashTable.bucket()[0].value().val);
}

TEST(HashTable, add_full) {
    int universal = 2;
    dsa::HashTable<int, std::string> hashTable(universal);
    hashTable.add(0, "red");
    hashTable.add(1, "green");
    hashTable.add(2, "blue");
    EXPECT_EQ(0, hashTable.bucket()[0].value().key);
    EXPECT_EQ("red", hashTable.bucket()[0].value().val);
    EXPECT_EQ(1, hashTable.bucket()[1].value().key);
    EXPECT_EQ("green", hashTable.bucket()[1].value().val);
}


TEST(HashTable, get) {
    int universal = 3;
    dsa::HashTable<int, std::string> hashTable(universal);
    hashTable.add(0, "red");
    hashTable.add(1, "green");
    hashTable.add(3, "blue");
    EXPECT_EQ("red", hashTable.get(0).value().val);
    EXPECT_EQ("green", hashTable.get(1).value().val);
    ASSERT_TRUE(!hashTable.get(2).has_value());
}
