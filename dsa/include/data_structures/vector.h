#include <cstddef>
#include <iostream>
#include <memory>
#include <stdexcept>
namespace dsa {

template <typename T>

class Vector {
private:
  size_t size_;
  size_t capacity_;
  std::unique_ptr<T[]> arr_;

public:
  Vector() : size_(0), capacity_(16) {
    // always allocated capacity of arrays as twice as param size
    arr_ = std::make_unique<T[]>(capacity_);
  }
  size_t size() { return size_; }
  size_t capacity() { return capacity_; }
  void push(T val) {
    if (size_ + 1 >= capacity_) {
      capacity_ <<= 1;
      std::unique_ptr<T[]> nw_arr = std::make_unique<T[]>(capacity_);
      for (auto i = 0; i < size_; ++i) {
        nw_arr[i] = arr_[i];
      }
      arr_ = std::move(nw_arr);
    }
    arr_[size_] = val;
    ++size_;
  }

  T &at(size_t index) {
    if (index >= size_) {
      throw std::out_of_range("index out of bounds");
    }
    return arr_[index];
  }

  void insert(size_t index, T val) {
    push(val);
    for (size_t i = size_ - 1; i > index; --i) {
      auto tmp = arr_[i - 1];
      arr_[i - 1] = arr_[i];
      arr_[i] = tmp;
    }
  }

  void prepend(T val) { insert(0, val); }

  bool is_empty() { return size_ == 0; }

  T &pop() {
    if (size_ > 0) {
      return arr_[--size_];
    }
    throw std::out_of_range("pop empty vector");
  }

  void del(size_t index) {
    if (size_ <= 0 || index >= size_) {
      throw std::out_of_range("out of bound");
    }
    if (index == size_ - 1) {
      pop();
    } else {
      for (size_t i = index; i < size_ - 1; ++i) {
        arr_[i] = arr_[i + 1];
      }
      --size_;
    }
  }
};
} // namespace dsa
