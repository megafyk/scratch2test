class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # bfs + custom dijkstra
        # time O(m*n), space O(m*n)
        m, n = len(grid), len(grid[0])
        cur = health - grid[0][0]
        if cur <= 0:
            return False
        dist = [[-inf] * n for _ in range(m)]
        dist[0][0] = cur

        q = deque()
        q.append((grid[0][0], 0, 0))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while q:
            cost, x, y = q.popleft()
            if (x, y) == (m - 1, n - 1):
                return True
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nw_dist = dist[x][y] - grid[nx][ny]
                    if nw_dist > 0 and nw_dist > dist[nx][ny]:
                        dist[nx][ny] = nw_dist
                        # prefer next path with no cost
                        if grid[nx][ny] == 0:
                            q.appendleft((grid[nx][ny], nx, ny))
                        else:
                            q.append((grid[nx][ny], nx, ny))
        return False


class Solution1:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # dijkstra
        # time O(m*nlog(m*n)), space O(m*n)
        m, n = len(grid), len(grid[0])
        cur = health - grid[0][0]
        if cur <= 0:
            return False
        pq = [(-cur, 0, 0)]
        dist = [[-inf] * n for i in range(m)]
        dist[0][0] = cur
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while pq:
            h, x, y = heappop(pq)
            h = -h
            if (x, y) == (m - 1, n - 1):
                return True
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nh = h - grid[nx][ny]
                    if nh > 0 and nh > dist[nx][ny]:
                        dist[nx][ny] = nh
                        heappush(pq, (-nh, nx, ny))
        return False
