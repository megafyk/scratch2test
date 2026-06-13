#include <cstddef>
#include <memory>
namespace dsa {

template <typename T>

class Vector {
private:
  size_t size_;
  size_t capacity_;
  std::unique_ptr<T[]> array_;

public:
  Vector(): size_(0), capacity_(16) {
    // always allocated capacity of arrays as twice as param size
    array_ = std::make_unique<T[]>(capacity_);
  }
  size_t size() { return size_; }
  size_t capacity() { return capacity_; }
  void push(T val) {
    if (size_ + 1 >= capacity_) {
      capacity_ <<= 1;
      std::unique_ptr<T[]> nw_arr = std::make_unique<T[]>(capacity_);
      for (auto i = 0; i < size_; ++i) {
        nw_arr[i] = array_[i];
      }
      array_ = std::move(nw_arr);
    }
    array_[size_] = val;
    ++size_;
  }

  T& at(size_t index) {
      if(index >= size_) {
          throw std::out_of_range("index out of bounds");
      }
      return array_[index];
  }
};
} // namespace dsa
