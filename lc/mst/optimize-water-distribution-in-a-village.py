from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def minCostToSupplyWater(self, n, wells, pipes):
        # prim's algo
        # m = len(wells)
        # time O(nlogn), space O(n)
        adj = defaultdict(list)
        for v, cost in enumerate(wells):
            adj[0].append((cost, v + 1))
            adj[v + 1].append((cost, 0))

        for u, v, cost in pipes:
            adj[u].append((cost, v))
            adj[v].append((cost, u))

        pq = [(0, 0)]  # dist, node
        visit = set()
        mi_cost = 0
        while pq and len(visit) < n + 1:
            c, u = heappop(pq)
            if u in visit:
                continue
            visit.add(u)
            mi_cost += c
            for cost, v in adj[u]:
                if v not in visit:
                    heappush(pq, (cost, v))
        return mi_cost


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]

    def find(self, u):
        if u != self.par[u]:
            self.par[u] = self.find(self.par[u])
        return self.par[u]

    def union(self, u, v):
        p1 = self.find(u)
        p2 = self.find(v)
        if p1 == p2:
            return False
        if p1 < p2:
            self.par[p2] = p1
        else:
            self.par[p1] = p2
        return True


class Solution1:
    def minCostToSupplyWater(self, n, wells, pipes):
        # kruskal
        # time O(nlogn), space O(n)
        for v, c in enumerate(wells):
            pipes.append([0, v + 1, c])
        pipes.sort(key=lambda x: x[-1])
        uf = UnionFind(n + 1)

        cnt_edges = 0
        mi_cost = 0
        for u, v, w in pipes:
            if uf.union(u, v):
                mi_cost += w
                cnt_edges += 1
                if cnt_edges == n:
                    return mi_cost
        return -1
