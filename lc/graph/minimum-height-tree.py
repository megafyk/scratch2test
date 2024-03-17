from collections import deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        degree = [0 for _ in range(n)]
        graph = [[] for _ in range(n)]
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
            degree[v1] += 1
            degree[v2] += 1

        q = deque([i for i in range(n) if degree[i] == 1])

        while n > 2:
            n -= len(q)
            next_q = deque()
            while q:
                u = q.popleft()
                for v in graph[u]:
                    degree[v] -= 1
                    if degree[v] == 1:
                        next_q.append(v)
            q = next_q

        res = []
        while q:
            res.append(q.popleft())
        return res
