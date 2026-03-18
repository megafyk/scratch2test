class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        # prefix sum 2d array
        # time O(m*n), space O(1)
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                s = grid[i][j]
                if i-1>=0:
                    s += grid[i-1][j]
                if j-1>=0:
                    s += grid[i][j-1]
                if i-1>=0 and j-1>=0:
                    s -= grid[i-1][j-1]
                grid[i][j] = s
                cnt += 1 if s <= k else 0
        return cnt