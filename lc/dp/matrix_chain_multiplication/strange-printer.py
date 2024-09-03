class Solution:
    def dp(self, s, memo, i, j):
        if i > j:
            return 0
        
        if memo[i][j] != sys.maxsize:
            return memo[i][j]

        mi = self.dp(s, memo, i + 1, j) + 1
        for k in range(i + 1, j + 1):
            if s[k] == s[i]:
                mi = min(mi, self.dp(s, memo, i, k - 1) + self.dp(s, memo, k + 1, j))
        memo[i][j] = mi
        return mi

    def strangePrinter(self, s: str) -> int:
        n = len(s)
        memo = [[sys.maxsize] * n for _ in range(n)]
        return self.dp(s, memo, 0, n - 1)

    # def strangePrinter(self, s: str) -> int:
    #     # dp topup
    #     # complexity: time O(n^3), mem O(n^2)
    #     if not s:
    #         return 0
    #     n = len(s)
    #     dp = [[sys.maxsize] * n for _ in range(n)]

    #     for i in range(n):
    #         dp[i][i] = 1

    #     for length in range(2, n+1):
    #         for i in range(n - length + 1):
    #             j = i + length - 1
    #             dp[i][j] = dp[i+1][j] + 1
    #             for k in range(i + 1, j + 1):
    #                 if s[i] == s[k]:
    #                     dp[i][j] = min(
    #                         dp[i][j], dp[i][k - 1] + (dp[k + 1][j] if k < j else 0)
    #                     )
    #     return dp[0][n - 1]
