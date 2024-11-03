class Solution:
    def isCircularSentence(self, s: str) -> bool:
        n = len(s)

        if n < 3: return s[0] == s[-1]
        for i in range(1, n-1):
            if s[i] == " " and s[i-1] != s[i+1]: return False
        return s[0] == s[-1]
