class TrieNode:
    def __init__(self):
        self.child = {}
        self.isfolder = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # trie
        # time O(nlogn + )
        folder.sort(key = lambda x: len(x))
        
        trie = Trie()
        for f in folder:
            node = trie.root
            words = f.split("/")[1:]
            for i, w in enumerate(words):
                if node.isfolder: # optimize
                    break
                if w not in node.child:
                    node.child[w] = TrieNode() 
                node = node.child[w]
                if i == len(words) - 1:
                    node.isfolder = True
        
        res = []
        def search(node, prefix):
            if node.isfolder:
                res.append(prefix)
                return
            for k,v in node.child.items():
                search(v, prefix + "/" + k)
        search(trie.root, "")
        return res


class TrieNode1:
    def __init__(self):
        self.exists = False
        self.child = {}
class Trie1:
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
class Solution1:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # time O(n*m + nlogn), space O(n*m)
        trie = Trie(sorted(folder))
        return list(trie.path)
