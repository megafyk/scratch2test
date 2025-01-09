class TrieNode:
    def __init__(self):
        self.child = {}
        self.word = True

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, w):
        cur = self.root
        for c in w:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]

        cur.word = True

    def search(self, w):
        cur = self.root
        for c in w:
            if c not in cur.child:
                return False
            cur = cur.child[c]
        
        return True

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        # trie prefix matching
        # time O(n*L + m), space O(m) 
        trie = Trie()
        trie.insert(s)
        res = 0
        for w in words:
            if trie.search(w):
                res += 1
        return res

# class Solution:
#     def countPrefixes(self, words: List[str], s: str) -> int:
#         # brute force
#         # time O(n^2), space O(1)
#         res = 0
#         for w in words:
#             if s.startswith(w):
#                 res += 1
#         return res
