class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]

    def find(self, u):
        if u != self.par[u]:
            u = self.find(self.par[u])
        return self.par[u]

    def union(self, u, v):
        p1 = self.find(u)
        p2 = self.find(v)
        if p1 == p2:
            return
        elif p1 < p2:
            self.par[p2] = p1
        else:
            self.par[p1] = p2


class Solution:
    def minimumCost(
        self, n: int, edges: List[List[int]], query: List[List[int]]
    ) -> List[int]:
        # graph + bitwise
        # time O(E + Q), space O(V)
        # COT
        # find minimum cost -> dijkstra
        # but bitwise AND make cost smaller and smaller: 0011 & 0010 = 0010
        # then vertices in a same connected component have same small cost
        # use unionfind to find connected components
        # then preprocess cost for each components
        uf = UnionFind(n)

        for u, v, w in edges:
            uf.union(u, v)

        components_cost = {}
        for u, v, w in edges:
            r = uf.find(u)
            if r not in components_cost:
                components_cost[r] = w
            else:
                components_cost[r] &= w
        res = []
        for src, dst in query:
            p1 = uf.find(src)
            p2 = uf.find(dst)
            if p1 != p2:
                res.append(-1)
            else:
                res.append(components_cost[p1])
        return res
