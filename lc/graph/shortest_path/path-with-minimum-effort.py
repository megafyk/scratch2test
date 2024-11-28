from heapq import heappop, heappush


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])

        visited = set()

        pq = [(0, 0, 0)]
        dis = [[float("inf")] * col for _ in range(row)]
        dis[0][0] = 0
        adj = [(0, -1), (-1, 0), (1, 0), (0, 1)]

        while pq:
            d, i, j = heappop(pq)

            if i + 1 == row and j + 1 == col:
                return d

            visited.add((i, j))

            for dx, dy in adj:
                x = i + dx
                y = j + dy

                if x >= row or x < 0 or y >= col or y < 0:
                    continue
                if (x, y) in visited:
                    continue

                new_diff = abs(heights[x][y] - heights[i][j])
                max_diff = max(new_diff, dis[i][j])
                if max_diff < dis[x][y]:
                    dis[x][y] = max_diff
                    heappush(pq, (max_diff, x, y))

        return 0
