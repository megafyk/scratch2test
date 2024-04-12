class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.isword = False
    
class WordDictionary:
    
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            idx = ord(c) - ord('a')
            if not curr.child[idx]:
                curr.child[idx] = TrieNode()
            curr = curr.child[idx]
        
        curr.isword = True
    
    def search_word(self, word, node, pos):
        if not word:
            return False
        curr = node
        for i in range(pos, len(word)):
            if word[i] == '.':
                for child in curr.child:
                    if child and self.search_word(word, child, i+1):
                        return True
                return False
            else:
                idx = ord(word[i]) - ord('a')
                if not curr.child[idx]:
                    return False
                curr = curr.child[idx]
        return curr.isword

    def search(self, word: str) -> bool:
        return self.search_word(word, self.root, 0)
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)