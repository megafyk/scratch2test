from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def dijkstra(self, adj, n, k):
        dis = [float('inf')] * n 
        dis[k-1] = 0
        pq = []
        heappush(pq, (k, 0))

        while pq:
            u, dist = heappop(pq)
            for v, w in adj[u]:
                cur_dist = dist + w
                if cur_dist < dis[v-1]:
                    dis[v-1] = cur_dist
                    heappush(pq, (v, dis[v-1]))

        return dis

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # complexity: time O(v+e), mem(v)
        adj = defaultdict(list)

        for u,v,w in times:
            adj[u].append((v, w))

        dis = self.dijkstra(adj, n, k)
        return -1 if float('inf') in dis else max(dis)