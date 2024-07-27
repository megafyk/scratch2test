class Solution:
    def numSquares(self, n: int) -> int:
        # dp
        # complexity: time O(n), mem O(n)
        dp = [float("inf") for _ in range(n + 1)]
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1
            mi = float("inf")
            while j * j <= i:
                mi = min(mi, dp[i - j * j] + 1)
                j += 1
            dp[i] = mi
        return dp[-1]
