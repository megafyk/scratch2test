#pragma once
#include <cstddef>
namespace dsa::data_structures::arrays
{
template <typename T> class Mvector
{
  private:
    std::size_t size_;
    std::size_t capacity_;
    T *data_;
    
  public:
    Mvector();
    ~Mvector();

    std::size_t size();
};

} // namespace dsa::data_structures::arrays
