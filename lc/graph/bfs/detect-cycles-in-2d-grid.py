class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # dfs
        # time O(m*n), space O(m*n)
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visit = set()

        def dfs(x, y, par):
            if (x, y) in visit:
                return True
            visit.add((x, y))
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < m
                    and 0 <= ny < n
                    and (nx, ny) != par
                    and grid[nx][ny] == grid[x][y]
                ):
                    if dfs(nx, ny, (x, y)):
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if (i, j) not in visit:
                    if dfs(i, j, (-1, -1)):
                        return True
        return False
