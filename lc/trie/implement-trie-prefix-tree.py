class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.endword = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            idx = ord(c) - ord('a')
            if not curr.child[idx]:
                curr.child[idx] = TrieNode()
            curr = curr.child[idx]
        
        curr.endword = True


    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            idx = ord(c) - ord('a')
            if not curr.child[idx]:
                return False
            curr = curr.child[idx]
        
        return curr.endword

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            idx = ord(c) - ord('a')
            if not curr.child[idx]:
                return False
            curr = curr.child[idx]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)