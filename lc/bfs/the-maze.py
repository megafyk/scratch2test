from typing import (
    List,
)

from collections import deque

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """

    def is_not_wall(self,x,y,rows,cols,maze):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0

    def has_path(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # basic bfs graph traversal
        # complexity: time O(r*m), mem O(1)
        rows = len(maze)
        cols = len(maze[0])

        dirs = [(0,1),(1,0),(-1,0),(0,-1)]

        q = deque([(start[0], start[1])])
        visited = set()
        while q:
            x,y = q.popleft()
            visited.add((x,y))

            for dx,dy in dirs:
                new_x, new_y = x,y
                while(self.is_not_wall(new_x+dx, new_y+dy, rows, cols, maze)):
                    new_x += dx
                    new_y += dy
                
                if (new_x, new_y) in visited:
                    continue
                if new_x == destination[0] and new_y == destination[1]:
                    return True
                q.append((new_x, new_y))
        return False