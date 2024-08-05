class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # complexity: time O(m*n), mem O(n)
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]

    # def uniquePaths(self, m: int, n: int) -> int:
    #     if m == 1 or n == 1: return 1
    #     dp = [[0] * n for _ in range(m)]
    #     dp[0][1], dp[1][0] = 1, 1
    #     for i in range(m):
    #         for j in range(n):
    #             if j-1 >= 0: dp[i][j] += dp[i][j-1]
    #             if i-1 >= 0: dp[i][j] += dp[i-1][j]
    #     return dp[-1][-1]
