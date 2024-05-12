from typing import (
    List,
)
from heapq import heappush, heappop

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    def is_not_wall(self, x, y, rows, cols, maze):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0 

    def shortest_distance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])

        dis = [[float('inf')] * cols for _ in range(rows)]
        dis[start[0]][start[1]] = 0
        # pq min heap
        pq = [(start[0],start[1])]
        d = [(0,1),(1,0),(-1,0),(0,-1)]

        while pq:
            x,y = heappop(pq)
            for dx,dy in d:
                new_x, new_y = x,y
                cnt = dis[x][y]
                while(self.is_not_wall(new_x+dx, new_y+dy, rows, cols, maze)):
                    new_x += dx
                    new_y += dy
                    cnt += 1
                if cnt < dis[new_x][new_y]:
                    dis[new_x][new_y] = cnt
                    if new_x == destination[0] and new_y == destination[1]:
                        continue
                    heappush(pq, (new_x, new_y))
        res = dis[destination[0]][destination[1]]
        return res if res != float('inf') else -1