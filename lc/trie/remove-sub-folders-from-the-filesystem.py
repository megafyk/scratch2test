class TrieNode:
    def __init__(self):
        self.exists = False
        self.child = {}
class Trie:
    def __init__(self, arr):
        self.root = TrieNode()
        self.path = set()
        for f in arr:
            cur = self.root
            add = True
            for part in f.split("/")[1:]:
                if part not in cur.child:
                    cur.child[part] = TrieNode()
                cur = cur.child[part]
                if cur.exists:
                    add = False
                    break
            cur.exists = True
            if add: self.path.add(f)
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # time O(n*m + nlogn), space O(n*m)
        trie = Trie(sorted(folder))
        return list(trie.path)
