from heapq import heappush, heappop

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # dijkstra, w = 0 if grid[x][y] == sign else 1
        # complexity: time O(r*c + 4*r*c*log(r*c)), mem O(r*c)
        rows = len(grid)
        cols = len(grid[0])

        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0
        pq = [(0,0,0)]
        dirs = [(0,1,1),(1,0,3),(-1,0,4),(0,-1,2)]
        visited = set()

        while pq:
            d,x,y = heappop(pq)
            visited.add((x,y))
            for dx,dy,sign in dirs:
                new_x,new_y = x+dx,y+dy
                if (new_x,new_y) in visited:
                    continue
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    w = 0 if grid[x][y] == sign else 1
                    cur_dist = dist[x][y] + w
                    if cur_dist < dist[new_x][new_y]:
                        dist[new_x][new_y] = cur_dist
                        heappush(pq, (dist[new_x][new_y],new_x,new_y))
        return dist[-1][-1]