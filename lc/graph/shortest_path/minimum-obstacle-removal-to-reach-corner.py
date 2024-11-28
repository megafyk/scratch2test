class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # djikstra
        # time O((V+E)logV), space O(V)
        m = len(grid)
        n = len(grid[0])
        dist = [[sys.maxsize] * n for _ in range(m)]

        dist[0][0] = 0
        pq = [(0,0,0)]
        while pq:
            w,x,y = heappop(pq)

            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nw_x, nw_y = x + dx, y + dy
                if 0 <= nw_x < m and 0 <= nw_y < n:
                    nw_w = w + grid[nw_x][nw_y]
                    if dist[nw_x][nw_y] > nw_w:
                        dist[nw_x][nw_y] = nw_w
                        heappush(pq, (nw_w, nw_x, nw_y))
        return dist[-1][-1]
