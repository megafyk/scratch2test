#pragma once
#include <cstddef>
namespace dsa {

template <typename Key, typename Value>

class HashTable {
private:
  struct Data {
    Key key;
    Value val;
  };
  std::size_t size_;
  Data data_[];

public:
  void add(Key key, Value val);
  bool exists(Key key);
  Value get(Key key);
  void remove(Key key);
};
} // namespace dsa
