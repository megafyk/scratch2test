class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # dp distinct ways
        # time O(n*m), space O(m)
        m = len(grid)
        n = len(grid[0])
        dp = [1] * m
        mx = 0
        for j in range(1, n):
            tmp_dp = [0] * m
            for i in range(m):
                for dx in [-1,0,1]:
                    x = i+dx
                    if 0 <= x < m and grid[i][j] > grid[x][j-1] and dp[x] > 0:
                        tmp_dp[i] = max(tmp_dp[i], dp[x] + 1)
                        mx = max(mx, tmp_dp[i]-1)
            dp = tmp_dp
        return mx
