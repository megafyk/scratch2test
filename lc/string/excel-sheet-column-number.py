class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        base = 26 
        res = 0
        for ch in columnTitle:
            res = res * base + (ord(ch) - ord("A") + 1)
        return res