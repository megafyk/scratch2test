#pragma once

#include <cstddef>
namespace dsa {

template <typename T>

class Deque {
private:
  class Node {
  public:
    T val;
    Node *next;
    Node *prev;
    Node(T val) : val(val) {}
  };

  Node *head_;
  Node *tail_;
  size_t size_;

public:
  size_t size();
  bool empty();
  T value_at(size_t idx);
  void push_front(T val);
  void pop_front();
  void push_back(T val);
  void pop_back();
  T front();
  T back();
  void insert(size_t idx, T val);
  void erase(size_t idx);
  T value_n_from_end(size_t n);
  void reverse();
  void remove_value(T val);
};
} // namespace dsa
