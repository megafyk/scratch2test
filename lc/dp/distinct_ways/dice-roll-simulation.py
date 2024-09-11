class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # complexity: time O(n*6^2*16^2), mem O(n*6*16)
        mod = 10 ** 9 + 7
        # dp[i][j][k] = #ways (i rolls . j face . k consecutive)
        dp = [[[0] * 16 for _ in range(6)] for _ in range(n+1)]
        for i in range(6):
            dp[1][i][1] = 1

        for i in range(1, n+1):
            for j in range(6):
                for k in range(1, rollMax[j] + 1):
                    if k == 1: # roll number j once
                        for jj in range(6):
                            if jj != j:
                                for kk in range(1, rollMax[jj] + 1):
                                    dp[i][j][k] = dp[i][j][k] +dp[i-1][jj][kk]
                    elif k > 1: # roll number j consecutive 
                        dp[i][j][k] = dp[i-1][j][k-1]
                    
                
        ans = 0
        for j in range(6):
            for k in range(1, rollMax[j] + 1):
                ans += dp[n][j][k]
        return ans % mod
