class UnionFind:
    def __init__(self):
        self.par = {}
        self.weight = {}

    def find(self, u):
        if u != self.par[u]:
            org = self.par[u]
            self.par[u] = self.find(self.par[u])
            self.weight[u] *= self.weight[org]
        return self.par[u]

    def union(self,u,v,val):
        if u not in self.par: 
            self.par[u] = u
            self.weight[u] = 1
        if v not in self.par:
            self.par[v] = v
            self.weight[v] = 1
        
        p1 = self.find(u)
        p2 = self.find(v)

        if p1 != p2:
            self.par[p1] = p2
            self.weight[p1] = val * self.weight[v] / self.weight[u]

    def ratio(self,u,v):
        if u in self.par and v in self.par and self.find(u) == self.find(v):
            return self.weight[u] / self.weight[v]
        return -1

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # graph union find
        # time O(e + q), space O(e + q)
        uf = UnionFind()
        for (x,y), val in zip(equations, values):
            uf.union(x,y,val)
        
        return [uf.ratio(x,y) for x,y in queries]