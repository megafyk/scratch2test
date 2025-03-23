class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # graph dijikstra + dp
        # time O((V+E)*logV), space O(V)
        MOD = 10**9 + 7
        dist = [sys.maxsize] * n
        dist[0] = 0
        adj = defaultdict(list)
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))

        pq = [(0, 0)]
        path_count = [0] * n
        path_count[0] = 1  # dp

        while pq:
            dst, u = heappop(pq)

            for v, w in adj[u]:
                tmp = dst + w
                if (
                    tmp < dist[v]
                ):  # why not tmp <= dist[v] -> exponential complexity when has multiple vertices have same distance
                    dist[v] = tmp
                    path_count[v] = path_count[u]
                    heappush(pq, (tmp, v))
                elif tmp == dist[v]:
                    path_count[v] += path_count[u]
        return path_count[-1] % MOD
