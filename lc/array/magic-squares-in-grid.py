class Solution:
    def is_magic_square(self, grid, cell):
        x, y = cell

        s = set()
        for i in range(-1, 2):
            for j in range(-1, 2):
                s.add(grid[x + i][y + j])

        if s != set(range(1, 10)):
            return False

        # check rows
        row1 = grid[x - 1][y - 1] + grid[x - 1][y] + grid[x - 1][y + 1]
        row2 = grid[x][y - 1] + grid[x][y] + grid[x][y + 1]
        row3 = grid[x + 1][y - 1] + grid[x + 1][y] + grid[x + 1][y + 1]
        if row1 != row2 != row3 != 15:
            return False
        # check columns
        col1 = grid[x - 1][y - 1] + grid[x][y - 1] + grid[x + 1][y - 1]
        col2 = grid[x - 1][y] + grid[x][y] + grid[x + 1][y]
        col3 = grid[x - 1][y + 1] + grid[x][y + 1] + grid[x + 1][y + 1]
        if col1 != col2 != col3 != 15:
            return False
        # check diagonals
        if (
            grid[x - 1][y - 1] + grid[x][y] + grid[x + 1][y + 1] != 15
            or grid[x - 1][y + 1] + grid[x][y] + grid[x + 1][y - 1] != 15
        ):
            return False
        return True

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        if n < 3 or m < 3:
            return 0
        ans = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                ans += 1 if self.is_magic_square(grid, (i, j)) else 0
        return ans
