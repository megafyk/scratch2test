#pragma once
#include <cstddef>
namespace dsa::data_structures::arrays
{
// A growable dynamic array (like std::vector) over a raw heap buffer.
// Implement every member below; no bodies are provided on purpose.
//
// Invariant to maintain: size_ <= capacity_, and data_ addresses storage for
// capacity_ elements (or is null when capacity_ == 0).
template <typename T> class Mvector
{
  private:
    std::size_t size_;     // number of constructed elements
    std::size_t capacity_; // allocated slots
    T *data_;              // owning pointer to the buffer

  public:
    // --- Rule of Five -------------------------------------------------------
    // Owning a raw pointer means you must define all five, or you get shallow
    // copies and double-frees. Implement each one.
    Mvector();                                    // O(1)
    Mvector(const Mvector &other);                // O(n) deep copy
    Mvector(Mvector &&other) noexcept;            // O(1) steal buffer
    Mvector &operator=(const Mvector &other);     // O(n)
    Mvector &operator=(Mvector &&other) noexcept; // O(1) steal buffer
    ~Mvector();                                   // O(n) destroy elements + free

    // --- Capacity -----------------------------------------------------------
    std::size_t size() const;     // O(1)
    std::size_t capacity() const; // O(1)
    bool empty() const;           // O(1)
    void reserve(std::size_t n);  // O(n) grow buffer to hold at least n elements

    // --- Element access -----------------------------------------------------
    // Pair each accessor so a const Mvector stays readable but immutable.
    T &operator[](std::size_t index);             // O(1), no bounds check
    const T &operator[](std::size_t index) const; // O(1), no bounds check
    T &front();                                    // O(1)
    const T &front() const;                        // O(1)
    T &back();                                     // O(1)
    const T &back() const;                         // O(1)

    // --- Modifiers ----------------------------------------------------------
    void push_back(const T &value); // amortized O(1); reallocates when full
    void pop_back();                // O(1)
    void clear();                   // O(n) destroy elements, keep capacity
};

} // namespace dsa::data_structures::arrays
