class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] number of unique BSTs with i nodes
        # complexity: time O(n^2), space O(n)
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]
