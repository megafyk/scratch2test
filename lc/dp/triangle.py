class Solution:
    def minimumTotal(self, dp: List[List[int]]) -> int:
        # dp
        # complexity: time O(nlogn), mem O(1)
        n = len(dp)
        for i in range(1, len(dp)):
            for j in range(len(dp[i])):
                if j > 0 and j < len(dp[i - 1]):
                    dp[i][j] = dp[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j])
                elif j < len(dp[i - 1]):
                    dp[i][j] = dp[i][j] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j] + dp[i - 1][j - 1]
        return min(dp[-1])
