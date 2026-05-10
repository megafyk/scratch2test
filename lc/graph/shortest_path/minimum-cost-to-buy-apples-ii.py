class Solution:
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
        # dijkstra
        # time O(V * (V + ElogE)), space O(V)
        adj = defaultdict(list)

        for u, p in enumerate(prices):
            adj[u].append((u + n, p))
            adj[u + n].append((u, 0))

        for u, v, cost, tax in roads:
            adj[u].append((v, cost))
            adj[v].append((u, cost))
            adj[u + n].append(
                (v + n, cost * tax)
            )  # tricky part, back from buy store to home store
            adj[v + n].append((u + n, cost * tax))

        def min_cost(start):
            dist = [inf] * 2 * n
            dist[start] = 0
            pq = [(0, start)]  # min heap (cost, u)
            target = start + n  # alway back to home store
            mi_cost = inf
            while pq:
                cost, u = heappop(pq)

                if u == target:
                    return cost
                for v, c in adj[u]:
                    nw_cost = cost + c
                    if nw_cost < dist[v]:
                        dist[v] = nw_cost
                        heappush(pq, (nw_cost, v))

            return mi_cost

        res = [0] * n
        for i in range(n):
            res[i] = min_cost(i)
        return res
