class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vow = con = False
        word = word.lower()
        for c in word:
            if c.isalpha() or c.isdigit():
                if c in "aeiou":
                    vow = True
                elif c not in "0123456789":
                    con = True
            else:
                return False
        return vow and con