from typing import (
    List,
)
from collections import deque
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        # bfs graph matrix
        # time O(m*n), space O(m*n)
        m = len(rooms)
        n = len(rooms[0])
        q = deque()
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i,j,0))

                while q:
                    for _ in range(len(q)):
                        x,y,dist = q.popleft()
                        for dx,dy in dirs:
                            nx,ny,nd = x+dx,y+dy,dist+1
                            if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] != -1 and rooms[nx][ny] != 0 and rooms[nx][ny] > nd:
                                rooms[nx][ny] = nd
                                q.append((nx,ny,nd))