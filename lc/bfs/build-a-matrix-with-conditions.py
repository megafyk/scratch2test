from collections import deque


class Solution:

    def topo(self, edges, n):
        indegree = [0] * (n + 1)
        order = []

        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1
        q = deque()
        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append(i)

        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        return order if len(order) == n else []

    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:
        # merge topo_row + topo_col == res[row][col]
        # complexity: time O(max(k^2, k+e)), mem O(max(k^2, k+e))
        res = [[0] * k for _ in range(k)]
        order_row = self.topo(rowConditions, k)
        order_col = self.topo(colConditions, k)
        if not order_row or not order_col:
            return []
        for i in range(k):
            for j in range(k):
                if order_row[i] == order_col[j]:
                    res[i][j] = order_row[i]
        return res
