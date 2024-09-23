class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp on string
        # complexity: time O(n^2), space O(n^2)
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for l in range(1, n):
            for i in range(0, n - l):
                j = i + l
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]
