from collections import deque


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # topo + dp
        # complexity: time O(V+E), mem O(26*V)

        n = len(colors)
        indegree = [0] * n
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            indegree[b] += 1
        q = deque()

        num_colors = 26
        dp = [[0] * num_colors for _ in range(n)]
        for idx, ind in enumerate(indegree):
            dp[idx][ord(colors[idx]) - ord("a")] = 1
            if ind == 0:
                q.append(idx)

        mx = 1
        while q:
            u = q.popleft()
            for v in adj[u]:
                indegree[v] -= 1
                # dp go from here
                for i in range(num_colors):
                    cnt = 1 if (ord(colors[v]) - ord("a")) == i else 0
                    dp[v][i] = max(dp[v][i], dp[u][i] + cnt)
                    mx = max(mx, dp[v][i])

                if indegree[v] == 0:
                    q.append(v)

        if max(indegree) != 0:
            return -1

        return mx
