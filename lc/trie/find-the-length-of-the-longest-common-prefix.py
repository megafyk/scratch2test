class TrieNode:
    def __init__(self):
        self.child = {}
        self.word = False


class Trie:
    def __init__(self, arr):
        self.root = TrieNode()
        for number in arr:
            # insert
            cur = self.root
            extract = str(number)
            for c in extract:
                if c not in cur.child:
                    cur.child[c] = TrieNode()
                cur = cur.child[c]
            cur.word = True


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # trie
        # complexity: time O(n2), space (m*n1)
        lcp = 0
        trie = Trie(arr1)
        for number in arr2:
            cur = trie.root
            extract = str(number)
            count = 0
            for c in extract:
                if c in cur.child:
                    count += 1
                else:
                    break
                cur = cur.child[c]
            lcp = max(lcp, count)
        return lcp


class Solution1:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # hashmap
        # time O(n1*m + n2*m), space O(n1*m)
        prefix = set()
        for num in arr1:
            s = str(num)
            for i in range(1, len(s) + 1):
                prefix.add(s[:i])
        lcp = 0
        for num in arr2:
            s = str(num)
            for i in range(1, len(s) + 1):
                if s[:i] in prefix:
                    lcp = max(lcp, i)
        return lcp
