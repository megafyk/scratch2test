#pragma once
#include <cstddef>
#include <functional>
namespace dsa::data_structures::hash_tables
{
// Separate-chaining hash map from Key to Value. Implement every member from
// scratch (inline here, since it is a template). Suggested build order:
//   1. Pick a bucket representation, e.g. an array of singly-linked-list nodes.
//   2. bucket_index(): reduce Hash{}(key) modulo bucket_count_.
//   3. insert(): find the bucket, overwrite on duplicate key, else prepend.
//   4. find()/contains()/erase(): walk the chain in the target bucket.
//   5. rehash(): allocate more buckets and re-distribute every entry.
//      Trigger it from insert() once load factor (size_ / bucket_count_) grows.
template <typename Key, typename Value, typename Hash = std::hash<Key>> class HashTable
{
  private:
    // TODO: declare your bucket storage here (e.g. a node* array + Hash hash_).
    std::size_t size_;         // number of stored key/value pairs
    std::size_t bucket_count_; // number of buckets

    std::size_t bucket_index(const Key &key) const; // O(1) map a key to a bucket
    void rehash(std::size_t new_bucket_count);       // O(n) grow + redistribute

  public:
    // --- Rule of Five (the table owns its bucket nodes) ---------------------
    HashTable();                                      // O(1)
    HashTable(const HashTable &other);                // O(n) deep copy
    HashTable(HashTable &&other) noexcept;            // O(1) steal buckets
    HashTable &operator=(const HashTable &other);     // O(n)
    HashTable &operator=(HashTable &&other) noexcept; // O(1) steal buckets
    ~HashTable();                                     // O(n) free every node

    // --- Lookup / modify (average O(1); worst O(n) on a degenerate chain) ---
    void insert(const Key &key, const Value &value); // insert or overwrite
    bool erase(const Key &key);                      // returns true if removed
    Value *find(const Key &key);                     // pointer to value, or nullptr
    const Value *find(const Key &key) const;         // const overload
    bool contains(const Key &key) const;

    std::size_t size() const; // O(1)
    bool empty() const;       // O(1)
};

} // namespace dsa::data_structures::hash_tables
