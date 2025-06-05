class UnionFind:
    def __init__(self, s1,s2):
        self.par = {}
        for i in range(len(s1)):
            self.par[s1[i]] = s1[i]
            self.par[s2[i]] = s2[i]
        

    def find(self, u):
        if u != self.par[u]:
            self.par[u] = self.find(self.par[u])
        return self.par[u]

    def union(self,u,v):
        p1 = self.find(u)
        p2 = self.find(v)

        if p1 < p2:
            self.par[p2] = p1
        else:
            self.par[p1] = p2


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # unionfind
        # time O(n), space O(n)
        uf = UnionFind(s1, s2)
        
        for i in range(len(s1)):
            uf.union(s1[i], s2[i])

        res = [''] * len(baseStr)
        for i,c in enumerate(baseStr):
            if c in uf.par:
                e = uf.find(c)
                res[i] = e
            else:
                res[i] = c
        return ''.join(res)