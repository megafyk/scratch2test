class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        # complexity: time O(m*n), mem O(n)
        m = len(grid)
        n = len(grid[0])

        dp = [0] * n
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: dp[j] = 0
                elif j > 0: dp[j] += dp[j-1]
        return dp[-1]


    # def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
    #     # complexity: time O(m*n), mem O(m*n)
    #     m = len(grid)
    #     n = len(grid[0])
    #     dp = [[0] * n for _ in range(m)]
    #     dp[0][0] = 1
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == 1:
    #                 dp[i][j] = 0
    #             else:
    #                 dp[i][j] += dp[i-1][j] if i-1 >= 0 else 0
    #                 dp[i][j] += dp[i][j-1] if j-1 >= 0 else 0
    #     return dp[-1][-1]
