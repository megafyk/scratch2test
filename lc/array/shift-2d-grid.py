class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # grid, time O(m*n), space O(k)
        m,n = len(grid), len(grid[0])
        cells = m*n
        k %= cells
        if k == 0:
            return grid

        prev = [0] * k
        for x, cell in enumerate(range(cells-k, cells)):
            i = cell // n
            j = cell % n
            prev[x] = grid[i][j]

        for cell in range(m*n):
            i = cell // n
            j = cell % n
            grid[i][j], prev[cell % k] = prev[cell % k], grid[i][j]

        return grid

class Solution1:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # grid, time O(k*m*n), space O(1)
        m,n = len(grid), len(grid[0])
        k %= (m*n)
        for _ in range(k):
            prev = grid[0][0]
            last = grid[m-1][n-1]
            for i in range(m):
                for j in range(n):
                    if i == 0 and j == 0:
                        continue
                    grid[i][j], prev = prev, grid[i][j]
            grid[0][0] = last
        return grid
