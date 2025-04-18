class Solution:
    def countAndSay(self, n: int) -> str:
        # string brute force
        # time O(N^k), space O(k)
        def rle(s):
            N = len(s)
            i = 0
            res = ''
            for j in range(N):
                if s[i] != s[j]:
                    res += str(j-i) + s[i]
                    i = j
            res += str(j-i+1) + s[i]
            return res

        res = '1'
        for i in range(n-1):
            res = rle(res)
        return res