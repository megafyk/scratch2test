class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # dp distinct ways
        # complexity: time O(n*6*15*6*15), time O(n*6*15)
        mod = 10**9 + 7
        # dp[n][dice number][consecutive times]
        dp = [[[0] * 16 for _ in range(6)] for _ in range(n)]
        for j in range(6):
            dp[0][j][1] = 1
        for i in range(n):
            for j in range(6):
                for k in range(1, rollMax[j] + 1):
                    if k > 1:
                        dp[i][j][k] = dp[i - 1][j][k - 1]
                    else:
                        # k == 1
                        for jj in range(6):
                            for kk in range(1, rollMax[jj] + 1):
                                if jj != j:
                                    dp[i][j][k] += dp[i - 1][jj][kk]

        ans = 0

        for j in range(6):
            for k in range(1, rollMax[j] + 1):
                ans += dp[n - 1][j][k]
        return ans % mod
