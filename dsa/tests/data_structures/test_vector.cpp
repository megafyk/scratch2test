#include "data_structures/vector.h"
#include <gtest/gtest.h>

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
  for (auto i = 0; i < 16; ++i) {
    vector.push(i);
  }
  vector.insert(10, 10);
  EXPECT_EQ(vector.capacity(), 32);
  EXPECT_EQ(vector.at(10), 10);
}

TEST(Vector, pop) {
  Vector<int> vector;
  for (auto i = 0; i < 16; ++i) {
    vector.push(i);
  }

  EXPECT_EQ(vector.pop(), 15);
  EXPECT_EQ(vector.size(), 15);
}

TEST(Vector, del) {
  Vector<int> vector;
  for (auto i = 0; i < 16; ++i) {
    vector.push(i);
  }
  std::cout << vector.size() << std::endl;
  vector.del(15);
  EXPECT_EQ(vector.at(14), 14);
  EXPECT_EQ(vector.size(), 15);
  vector.del(10);
  EXPECT_EQ(vector.at(10), 11);
  EXPECT_EQ(vector.size(), 14);
}

TEST(Vector, remove) {
  Vector<int> vector;
  for (auto i = 0; i < 16; ++i) {
    if(i%2==0) {
        vector.push(2);
    } else {
        vector.push(i);
    }
  }
  vector.remove(2);
  EXPECT_EQ(vector.size(), 8);
}

TEST(Vector, find) {
  Vector<int> vector;
  for (auto i = 0; i < 16; ++i) {
    vector.push(i);
  }
  EXPECT_EQ(vector.find(2), 2);
}
