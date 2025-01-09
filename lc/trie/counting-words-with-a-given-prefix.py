class TrieNode:
    def __init__(self):
        self.child = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
            cur.count += 1
    def count(self, word):
        cur = self.root
        for c in word:
            if c not in cur.child:
                return 0
            cur = cur.child[c]
        return cur.count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        for w in words:
            trie.insert(w)
        return trie.count(pref)

# class Solution:
#     def prefixCount(self, words: List[str], pref: str) -> int:
#         # string pattern matching brute force
#         # time O(n^2), space O(1)

#         res = 0
#         for w in words:
#             if w.startswith(pref):
#                 res += 1
#         return res
