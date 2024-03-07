from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        n = len(grid)
        m = len(grid[0])

        for y in range(n):
            for x in range(m):
                if grid[y][x] == "1":
                    q = deque()
                    q.append((x, y))
                    grid[y][x] = "0"
                    res += 1

                    while q:
                        xx, yy = q.popleft()

                        for xxx, yyy in [
                            (xx - 1, yy),
                            (xx + 1, yy),
                            (xx, yy - 1),
                            (xx, yy + 1),
                        ]:
                            if 0 <= xxx < m and 0 <= yyy < n and grid[yyy][xxx] == "1":
                                q.append((xxx, yyy))
                                grid[yyy][xxx] = "0"
        return res
