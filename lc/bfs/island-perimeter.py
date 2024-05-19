from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # bfs
        # complexity: time O(n), mem O(n)
        rows = len(grid)
        cols = len(grid[0])

        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        start = None
        for i in range(rows):
            if start: break
            for j in range(cols):
                if grid[i][j]:
                    start = (i, j)
                    break
        p = 0
        q = deque([start])
        added = set()
        added.add((start))
        while q:
            x,y = q.popleft()
            tmp = 4
            for dx,dy in dirs:
                new_x, new_y = x+dx, y+dy
                if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y]:
                    tmp -= 1
                    if (new_x, new_y) not in added:
                        added.add((new_x, new_y))
                        q.append((new_x, new_y))
            p += tmp
        return p

    # def islandPerimeter(self, grid: List[List[int]]) -> int:
    #     # p vs adjacent cells
    #     # complexity: time O(rows*cols), mem O(1)
    #     p = 0
    #     rows = len(grid)
    #     cols = len(grid[0])
    #     dirs = [(0,1), (1,0), (0,-1), (-1,0)] 
    #     for i in range(rows):
    #         for j in range(cols):
    #             if grid[i][j] == 1:
    #                 tmp = 4
    #                 for dx,dy in dirs:
    #                     x = dx + i
    #                     y = dy + j
    #                     if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
    #                         tmp -= 1
    #                 p += tmp
    #     return p