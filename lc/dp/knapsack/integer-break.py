class Solution:
    def integerBreak(self, n: int) -> int:
        # knapsack
        # time O(n^2), space O(n)
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1

        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * dp[i-j], j * (i-j))
        return dp[-1]
            