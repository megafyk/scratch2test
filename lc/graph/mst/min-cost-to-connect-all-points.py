class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
    def find(self, u):
        if u != self.par[u]:
            self.par[u] = self.find(self.par[u])
        return self.par[u]

    def union(self, u,v):
        p1 = self.find(u)
        p2 = self.find(v)
        if p1 == p2:
            return False
        if p1 < p2:
            self.par[p2] = p1
        else:
            self.par[p1] = p2
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # kruskal
        # time O(n^2log(n^2)), space O(n^2)
        edges = []
        n = len(points)
        for i in range(n-1):
            for j in range(i+1, n):
                u,v = points[i], points[j]
                w = abs(u[0] - v[0]) + abs(u[1] - v[1])
                edges.append((w, (i,j)))
        edges.sort()

        cnt_e = 0
        res = 0
        uf = UnionFind(n)
        for w, (i,j) in edges:
            if cnt_e == n-1:
                return res
            if uf.union(i, j):
                cnt_e += 1
                res += w
        return res
                
class Solution1:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # mst prim
        # time O(n^2logn), space O(n)
        pq = [(0, (points[0][0],points[0][1]))]
        visit = set()
        
        cnt_e = 0
        n = len(points)
        res = 0
        while pq and cnt_e < n:
            w, u = heappop(pq)
            if u in visit:
                continue
            res += w
            cnt_e += 1
            visit.add(u)
            for x,y in points:
                if (x,y) != u and ((x,y) not in visit):
                    nw_w = abs(u[0]-x) + abs(u[1]-y)
                    heappush(pq, (nw_w, (x,y)))
        return res