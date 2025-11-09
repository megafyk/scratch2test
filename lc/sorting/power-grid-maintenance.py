class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
    
    def find(self, u):
        if u != self.par[u]:
            self.par[u] = self.find(self.par[u])
        return self.par[u]

    def union(self, u,v):
        p1 = self.find(u)
        p2 = self.find(v)
        if p1 == p2: return
        if p1 < p2:
            self.par[p2] = p1
        else:
            self.par[p1] = p2

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(c)
        for u,v in connections:
            uf.union(u,v)
        comp = [SortedList() for _ in range(c+1)]

        for u in range(c+1):
            p = uf.find(u)
            comp[p].add((0, u))

        res = []
        status = [i for i in range(c+1)]
        
        for op, u in queries:
            p = uf.find(u)

            if op == 1:
                sl = comp[p]
                if status[u]:
                    res.append(u)
                elif sl[0][0] == 0:
                    res.append(sl[0][1])
                else:
                    res.append(-1)
            else:
                sl = comp[p]
                sl.remove((0, u))
                sl.add((u,u))
                status[u] = 0

        return res
