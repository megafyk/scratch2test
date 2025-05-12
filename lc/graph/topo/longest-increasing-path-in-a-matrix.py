from collections import deque
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        def inbound(x, y, m, n):
            return 0 <= x < m and 0 <= y < n

        indegree = [[0 for _ in range(m)] for _ in range(n)]

        for y in range(n):
            for x in range(m):
                for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if inbound(xx, yy, m, n) and matrix[yy][xx] < matrix[y][x]:
                        indegree[y][x] += 1

        q = deque()
        for y in range(m):
            for x in range(n):
                if indegree[y][x] == 0:
                    q.append((x, y))

        dp = [[1 for _ in range(m)] for _ in range(n)]

        while q:
            x, y = q.popleft()
            # all adjacent of cell(x,y)
            for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if inbound(xx, yy, m, n) and matrix[yy][xx] > matrix[y][x]:
                    indegree[yy][xx] -= 1
                    dp[yy][xx] = max(dp[yy][xx], dp[y][x] + 1)
                    if indegree[yy][xx] == 0:
                        q.append((xx, yy))

        return max(max(ele) for ele in dp)
