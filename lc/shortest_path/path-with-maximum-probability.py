from collections import defaultdict


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # basic dijkstra with max heap
        # complexity: time O(ElogV), mem O(V)
        adj = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            adj[u].append((v, succProb[i]))
            adj[v].append((u, succProb[i]))
        prop = [0] * n
        prop[start] = 1
        pq = [] #max heap
        heappush(pq, (-prop[start], start))

        while pq:
            p, u = heappop(pq)
            p = -p
            for v, w in adj[u]:
                new_p = w * prop[u]
                if new_p > prop[v]:
                    prop[v] = new_p
                    heappush(pq, (-new_p, v))
        return prop[end]
