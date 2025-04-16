class Solution:
    def convert(self, s: str, k: int) -> str:
        # string
        # time O(N), space O(N)
        if k == 1: return s
        res = [''] * k
        j = 0
        down = True
        for i in range(len(s)):
            res[j] += s[i]
            if j == 0: down = True
            elif j == k-1: down = False
            j += 1 if down else -1    
        return ''.join(res)