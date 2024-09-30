class Solution:
    def mx(self, n, slices):
        m = len(slices)
        dp1 = [0] * (n + 1)
        dp2 = [0] * (n + 1)
        for i in range(1, m + 1):
            tmp = [0] * (n + 1)
            for j in range(1, n + 1):
                tmp[j] = max(dp1[j], slices[i - 1] + (dp2[j - 1] if i >= 2 else 0))  # (not take)/(take) slices[i]
            dp2, dp1 = dp1, tmp
        return dp1[n]

    def maxSizeSlices(self, slices: List[int]) -> int:
        # complexity: time O(n^2), space O(n)
        n = len(slices) // 3
        return max(self.mx(n, slices[1:]), self.mx(n, slices[:-1]))

    # def mx(self, n, slices):
    #     m = len(slices)
    #     dp = [[0] * (n + 1) for _ in range(m + 1)] # dp[i][j] -> from 0 -> i take j pieces
    #     for i in range(1, m + 1):
    #         for j in range(1, n + 1):
    #             dp[i][j] = max(dp[i - 1][j], slices[i-1] + (dp[i - 2][j - 1] if i >= 2 else 0)) # (not take)/(take) slices[i]
    #     return dp[m][n]

    # def maxSizeSlices(self, slices: List[int]) -> int:
    #     # complexity: time O(n^2), space O(n^2)
    #     n = len(slices) // 3
    #     return max(self.mx(n, slices[1:]), self.mx(n, slices[:-1]))
