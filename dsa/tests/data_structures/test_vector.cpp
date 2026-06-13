#include <gtest/gtest.h>
#include "data_structures/vector.h"

using namespace dsa;

TEST(Vector, size) {
    Vector<int> vector;
    EXPECT_EQ(vector.size(), 0);
}

TEST(Vector, capacity) {
    Vector<int> vector;
    EXPECT_EQ(vector.capacity(), 16);
}

TEST(Vector, push) {
    Vector<int> vector;
    vector.push(10);
    EXPECT_EQ(vector.at(0), 10);
}

TEST(Vector, insert) {
    Vector<int> vector;
    for(auto i = 0; i < 16; ++i) {
        vector.push(i);
    }
    vector.insert(10, 10);
    EXPECT_EQ(vector.capacity(), 32);
    EXPECT_EQ(vector.at(10), 10);
}
