#pragma once
#include <cstddef>
#include <iterator>
#include <optional>
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
  std::vector<std::optional<Data>> bucket_;

public:
  HashTable(int size) : bucket_(size) { size_ = size; }
  std::vector<std::optional<Data>> &bucket() { return bucket_; }
  std::size_t size() { return size_; }
  void add(Key key, Value val) {
    size_t start = key % size_;
    size_t cur = start;
    size_t first_deleted_idx = -1;
    while (true) {
      std::optional<Data> cur_val = bucket_[cur];
      if (!cur_val.has_value()) {
        size_t target_idx = (first_deleted_idx == -1) ? cur : first_deleted_idx;
        bucket_[target_idx] = {key, val, "ACTIVE"};
        return;
      } else if (bucket_[cur].value().status == "TOMBSTONE") {
        if (first_deleted_idx == -1) {
          first_deleted_idx = cur;
        }
      } else {
        if (bucket_[cur].value().key == key) {
          // update key
          bucket_[cur] = {key, val, "ACTIVE"};
        }
      }
      cur = (cur + 1) % size_;
      if (cur == start and first_deleted_idx == -1) {
        // hashtable full
        return;
      }
    }
  }

  std::optional<Data> get(Key key) {
    size_t start = key % size_;
    size_t cur = start;

    while (true) {
      std::optional<Data> cur_val = bucket_[cur];
      if (!cur_val.has_value()) {
        break;
      } else if (cur_val.has_value() && cur_val.value().key == key) {
        return cur_val;
      }
      cur = (cur + 1) % size_;
      if (cur == start) {
        break;
      }
    }
    return std::nullopt;
  }

  bool exists(Key key) { return get(key) != std::nullopt; }

  void remove(Key key) {
    std::size_t start = key % size_;
    std::size_t cur = start;
    while (true) {
        auto& cur_data = bucket_[cur];
        if(!cur_data.has_value()) {
            return;
        } else {
            if(cur_data->key == key && cur_data->status == "ACTIVE") {
                cur_data->status = "TOMBSTONE";
                return;
            }
        }
        cur = (cur + 1) % size_;
        if (cur == start) {
            return;
        }
    }
  }
};
} // namespace dsa
