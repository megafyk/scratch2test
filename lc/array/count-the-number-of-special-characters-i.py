class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        cnt = 0
        for i in range(26):
            c = chr(ord("a") + i)
            if c.lower() in s and c.upper() in s:
                cnt += 1
        return cnt
