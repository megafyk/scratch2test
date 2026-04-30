class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        # dp on grid
        # time O(m*n*k), space O(n*k)
        m, n = len(grid), len(grid[0])
        dp = [[-1] * (k + 1) for _ in range(n)]
        dp[0][0] = 0

        def get_score_cost(i, j):
            if grid[i][j] == 0:
                return (0, 0)
            elif grid[i][j] == 1:
                return (1, 1)
            else:
                return (2, 1)

        for i in range(m):
            nw_dp = [[-1] * (k + 1) for _ in range(n)]
            for j in range(n):
                for cost in range(k + 1):
                    s, c = get_score_cost(i, j)
                    nw_cost = cost + c
                    if nw_cost <= k:
                        if dp[j][cost] >= 0:
                            nw_dp[j][nw_cost] = max(nw_dp[j][nw_cost], dp[j][cost] + s)
                        if nw_dp[j - 1][cost] >= 0 and j > 0:
                            nw_dp[j][nw_cost] = max(
                                nw_dp[j][nw_cost], nw_dp[j - 1][cost] + s
                            )
            dp = nw_dp

        return max(dp[-1])


class Solution1:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        # bfs on grid -> TLE because we have to explore all possible paths
        # time O(2^(m+n)), space O(m*n)
        m, n = len(grid), len(grid[0])
        q = deque()
        q.append((0, 0, 0, 0))
        res = -1
        dirs = [(0, 1), (1, 0)]

        def get_score_cost(i, j):
            if grid[i][j] == 0:
                return (0, 0)
            elif grid[i][j] == 1:
                return (1, 1)
            else:
                return (2, 1)

        while q:
            x, y, score, cost = q.popleft()
            if (x, y) == (m - 1, n - 1):
                res = max(res, score)
                continue
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    s, c = get_score_cost(nx, ny)
                    if cost + c <= k:
                        q.append((nx, ny, score + s, cost + c))
        return res
