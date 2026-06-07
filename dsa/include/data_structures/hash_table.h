#pragma once
#include <cstddef>
#include <string>
#include <vector>
namespace dsa {

template <typename Key, typename Value>

class HashTable {
private:
  struct Data {
    Key key;
    Value val;
    std::string status;
  };
  std::size_t size_;
  std::vector<Data> data_;

public:
  HashTable(int size) : data_(size) { size_ = size; }
  std::vector<Data> getData() { return data_; }
  std::size_t getSize() { return size_; }
  void add(Key key, Value val) {
    size_t start = key % size_;
    size_t cur = start;
    size_t first_deleted_idx = -1;
    while (true) {
      if (*data_[cur] == nullptr) {
        size_t target_idx = (first_deleted_idx == -1) ? cur : first_deleted_idx;
        data_[target_idx] = {key, val, "ACTIVE"};
        return;
      } else if (data_[cur].status == "TOMBSTONE") {
        if (first_deleted_idx == -1) {
          first_deleted_idx = cur;
        }
      } else {
        if (data_[cur].key == key) {
            // update key
            data_[cur] = {key, val, "ACTIVE"};
        }
      }
      cur = (cur + 1) % size_;
      if(cur == start and first_deleted_idx == -1) {
          // hashtable full
          return;
      }
    }
  }
  bool exists(Key key);
  Value get(Key key);
  void remove(Key key);
};
} // namespace dsa
