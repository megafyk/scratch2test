class Solution:
    def minCut(self, s: str) -> int:
        @cache
        def dp(start, end):
            if ispal[start][end]: return 0
            res = sys.maxsize
            for s in range(start, end):
                if ispal[start][s]:
                    res = min(res, dp(s+1, end) + 1)
            return res

        n = len(s)

        # ispal[i][j] -> check s[i:j+1] palindrome
        ispal = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    ispal[i][j] = j-i <= 2 or ispal[i+1][j-1]

        return dp(0, n-1)
