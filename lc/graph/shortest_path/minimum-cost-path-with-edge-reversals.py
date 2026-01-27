class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # dijkstra
        # time O(u+eloge), space O(u+e)
        adj = defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w*2))

        inf = sys.maxsize
        dist = [inf] * n
        dist[0] = 0
        pq = [(0,0)]
        while pq:
            w_u, u = heappop(pq)
            for v, w_v in adj[u]:
                nw_w =  w_u + w_v
                if dist[v] > nw_w:
                    dist[v] = nw_w
                    heappush(pq, (nw_w, v))
        return dist[n-1] if dist[n-1] != inf else -1