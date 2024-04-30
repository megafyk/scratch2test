class Solution:
    def longestPrefix(self, s: str) -> str:
        # complexity: time O(n), mem O(n)
        # calculate kmp table ~ longest prefix ~ suffix table
        j = 0
        n = len(s)
        kmp = [0] * n
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = kmp[j-1]
            
            if s[i] == s[j]:
                kmp[i] = j+1
                j+=1
        return "" if kmp[-1] == 0 else s[n-kmp[-1]:]