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
            return

        if p1 < p2:
            self.par[p2] = p1
        else:
            self.par[p1] = p2


class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        # graph union find
        # time O(eloge), space O(n)
        track = [0] * n
        comp = n

        edges.sort(key=lambda x: x[2])
        uf = UnionFind(n)

        for u, v, w in edges:
            if comp <= k:
                break

            p1 = uf.find(u)
            p2 = uf.find(v)

            if p1 != p2:
                uf.union(u, v)
                track[p1] = max(track[p1], w)
                track[p2] = max(track[p2], w)
                comp -= 1

        return max(track)