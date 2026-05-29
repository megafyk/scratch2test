#pragma once
// Copy-template for a new data structure. Steps:
//   1. Copy to include/dsa/data_structures/<category>/<name>.hpp
//   2. Rename the namespace segment and the class.
//   3. Replace the members with your structure's real interface.
// Implement the bodies inline (it is a template), declaration-by-declaration.
#include <cstddef>
namespace dsa::data_structures::your_category
{
// One line: what YourStructure is, and the invariant it must always uphold.
template <typename T> class YourStructure
{
  private:
    std::size_t size_; // TODO: replace with this structure's real state
    // TODO: add the storage your structure needs (pointer, array, nodes, ...).

  public:
    // Rule of Five: define all five whenever you own raw memory. If your
    // structure holds only value members (no manual new/delete), delete this
    // block and let the compiler generate them.
    YourStructure();                                          // O(?)
    YourStructure(const YourStructure &other);                // O(?)
    YourStructure(YourStructure &&other) noexcept;            // O(?)
    YourStructure &operator=(const YourStructure &other);     // O(?)
    YourStructure &operator=(YourStructure &&other) noexcept; // O(?)
    ~YourStructure();                                         // O(?)

    // Core interface: declare each operation, annotate its Big-O, implement
    // as you go.
    std::size_t size() const; // O(1)
    bool empty() const;       // O(1)
    // TODO: add insert / find / erase / ... for your structure.
};

} // namespace dsa::data_structures::your_category
