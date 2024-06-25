from collections import deque


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # topology sort
        # complexity: time O(V+E), mem O(n)
        n = len(quiet)
        ans = [i for i in range(n)]
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        q = deque()
        for a, b in richer:
            adj[a].append(b)
            indegree[b] += 1

        for idx, ind in enumerate(indegree):
            if ind == 0:
                q.append(idx)

        while q:
            u = q.popleft()

            for v in adj[u]:
                indegree[v] -= 1
                # basic dp go from here
                ans[v] = ans[u] if quiet[ans[u]] < quiet[ans[v]] else ans[v]

                if indegree[v] == 0:
                    q.append(v)
        return ans
