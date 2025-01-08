class TrieNode:
    def __init__(self):
        self.child = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, w):
        cur = self.root
        for c1,c2 in zip(w,reversed(w)):
            if (c1,c2) not in cur.child:
                cur.child[(c1,c2)] = TrieNode()
            cur = cur.child[(c1,c2)]
            cur.count += 1

    def count(self, w):
        cur = self.root
        for c1,c2 in zip(w, reversed(w)):
            if (c1,c2) not in cur.child:
                return 0
            cur = cur.child[(c1,c2)]
        return cur.count

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = Trie()
        res = 0
        for w in reversed(words):
            res += trie.count(w)
            trie.insert(w)
        return res
