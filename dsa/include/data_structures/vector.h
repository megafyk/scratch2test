#include <algorithm>
#include <cstddef>
#include <memory>
#include <stdexcept>
namespace dsa {

template <typename T>

class Vector {
private:
  size_t size_;
  size_t capacity_;
  std::unique_ptr<T[]> arr_;
  void resize() {
    bool rs = false;
    if (size_ == capacity_) {
      capacity_ <<= 1;
      rs = true;
    } else if (size_ <= capacity_ / 4 && capacity_ > 16) {
      capacity_ >>= 1;
      rs = true;
    }
    if (rs) {
      std::unique_ptr<T[]> nw_arr = std::make_unique<T[]>(capacity_);
      for (size_t i = 0; i < size_; ++i) {
        nw_arr[i] = arr_[i];
      }
      arr_ = std::move(nw_arr);
    }
  }

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

  T pop() {
    if (size_ > 0) {
      T val = arr_[--size_];
      resize();
      return val;
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

  void remove(T val) {
    bool found;
    for (size_t i = 0; i < size_; ++i) {
      if (arr_[i] == val) {
        found = true;
        break;
      }
    }
    if (!found)
      return;
    std::unique_ptr<T[]> nw_arr = std::make_unique<T[]>(capacity_);
    size_t nw_size = 0;
    for (size_t i = 0; i < size_; ++i) {
      if (arr_[i] == val) {
        continue;
      }
      nw_arr[nw_size++] = arr_[i];
    }
    arr_ = std::move(nw_arr);
    size_ = nw_size;
  }

  size_t find(T val) {
    for (size_t i = 0; i < size_; ++i) {
      if (arr_[i] == val) {
        return i;
      }
    }
    return -1;
  }
};
} // namespace dsa
