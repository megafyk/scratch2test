class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        pq = [(0,0,0)] # time,x,y
        visited = set()
        while pq:
            t,x,y = heappop(pq)

            if (x,y) == (m-1,n-1):
                return t

            if (x,y) in visited:
                continue

            visited.add((x,y))

            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nw_x, nw_y = x+dx, y+dy
                if 0 <= nw_x < m and 0 <= nw_y < n:
                    wait = 1 if (grid[nw_x][nw_y] - t) % 2 == 0 else 0
                    nxt = max(grid[nw_x][nw_y] + wait, t + 1)
                    heappush(pq, (nxt, nw_x, nw_y))
        return -1
