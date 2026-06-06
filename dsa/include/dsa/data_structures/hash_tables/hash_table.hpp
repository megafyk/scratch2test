#pragma once
#include <cstddef>
#include <functional>
namespace dsa::data_structures::hash_tables
{

template <typename Key, typename Value, typename Hash = std::hash<Key>>

class HashTable
{
  private:
    std::size_t size_;
    std::size_t bucket_count_;

  public:
    HashTable();
    HashTable(const HashTable &other);
    HashTable(HashTable &&other) noexcept;
    HashTable &operator=(const HashTable &other);
    HashTable &operator=(HashTable &&other) noexcept;
    ~HashTable();

    void hash(int m, Key k);
    void insert(Key k, Value v);
    void update(Key k, Value v);
    bool exists(Key k);
    Value get(Key k);
    void remove(Key k);
};

} // namespace dsa::data_structures::hash_tables
