class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # graph traversal with min heap
        # time O(m*n*log(m*n)), space O(m*n)
        m = len(heightMap)
        n = len(heightMap[0])

        res = 0
        pq = []  # min heap height
        # push boundary cell to pq first
        for r in range(m):
            for c in range(n):
                if (r == 0 or r == m - 1) or (c == 0 or c == n - 1):
                    heappush(pq, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1  # mark visited
        mx_height = -1
        res = 0
        while pq:
            h, x, y = heappop(pq)
            mx_height = max(mx_height, h)
            res += (mx_height - h)

            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in dirs:
                nw_x = x + dx
                nw_y = y + dy

                if 0 <= nw_x < m and 0 <= nw_y < n and heightMap[nw_x][nw_y] != -1:
                    heappush(pq, (heightMap[nw_x][nw_y], nw_x, nw_y))
                    heightMap[nw_x][nw_y] = -1

        return res
