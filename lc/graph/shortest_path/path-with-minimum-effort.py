class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # custom dijkstra
        # time O((m*n)log(m*n)), space O(m*n)
        m, n = len(heights), len(heights[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        dist = [[inf] * n for _ in range(m)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]  # min heap
        while pq:
            d, x, y = heappop(pq)
            if (x, y) == (m - 1, n - 1):
                return d
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nxt_d = max(d, abs(heights[x][y] - heights[nx][ny]))
                    if nxt_d < dist[nx][ny]:
                        dist[nx][ny] = nxt_d
                        heappush(pq, (nxt_d, nx, ny))
        return inf


class Solution1:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # binary search on result, find exists path with edge <= max_effort
        # time O(m*n + m*n*log(max(height))), space O(m*n)
        m, n = len(heights), len(heights[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        mx_effort = 0
        for x in range(m):
            for y in range(n):
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        mx_effort = max(mx_effort, abs(heights[x][y] - heights[nx][ny]))

        def path_exists(lim_effort):
            q = deque([(0, 0)])
            visit = set()
            visit.add((0, 0))
            while q:
                x, y = q.popleft()
                if (x, y) == (m - 1, n - 1):
                    return True
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < m
                        and 0 <= ny < n
                        and (nx, ny) not in visit
                        and abs(heights[x][y] - heights[nx][ny]) <= lim_effort
                    ):
                        q.append((nx, ny))
                        visit.add((nx, ny))
            return False

        l, r = 0, mx_effort
        while l < r:
            mid = l + (r - l) // 2
            if path_exists(mid):
                r = mid
            else:
                l = mid + 1
        return l
