from collections import deque
from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # bfs basic
        # complexity: time O(m*n), mem O(m*n)
        n, m = len(grid1), len(grid1[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid2[i][j] and (i, j) not in visited:
                    q = deque([(i, j)])
                    visited.add((i, j))
                    is_sub = True
                    while q:
                        x, y = q.popleft()
                        if grid1[x][y] == 0:
                            is_sub = False
                        for dx, dy in directions:
                            tmp_x, tmp_y = x + dx, y + dy
                            if (
                                0 <= tmp_x < n and 
                                0 <= tmp_y < m and 
                                grid2[tmp_x][tmp_y] and 
                                (tmp_x, tmp_y) not in visited
                            ):
                                q.append((tmp_x, tmp_y))
                                visited.add((tmp_x, tmp_y))
                    res += 1 if is_sub else 0
        return res
