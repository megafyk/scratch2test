class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod = 10 ** 9 + 7
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * k for _ in range(n)]
        r = 0
        for i in range(m):
            nw_dp = [[0] * k for _ in range(n)]
            for j in range(n):
                r = grid[i][j] % k
                
                if i == 0 and j == 0:
                    nw_dp[j][r] = 1
                    continue
                
                for kk in range(k):
                    nw_r = (kk+r) % k
                    nw_dp[j][nw_r] += ((nw_dp[j-1][kk] if j > 0 else 0) + dp[j][kk]) % mod
            dp = nw_dp
        
        return dp[-1][0]