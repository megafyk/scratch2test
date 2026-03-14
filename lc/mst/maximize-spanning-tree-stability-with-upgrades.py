from typing import List

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

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        uf = UnionFind(n)
        for u,v,w,m in edges:
            if m == 1:
                if not uf.union(u,v):
                    return -1

        uf_all = UnionFind(n)
        for u,v,w,m in edges:
            uf_all.union(u,v)

        if any([uf_all.find(i) != 0 for i in range(n)]):
            return -1

        def form_mst(min_edge):
            uf = UnionFind(n)
            cnt_edges = 0
            for u,v,w,m in edges:
                if m == 1:
                    if w < min_edge:
                        return False
                    uf.union(u,v)
                    cnt_edges += 1
            
            for u,v,w,m in edges:
                if m == 0:
                    if w >= min_edge and uf.union(u, v):
                        cnt_edges += 1
            
            cnt_upgrade = 0
            for u,v,w,m in edges:
                if m == 0:
                    if w < min_edge and w * 2 >= min_edge and uf.union(u, v):
                        cnt_edges += 1
                        cnt_upgrade += 1
                        if cnt_upgrade > k:
                            return False

            return cnt_edges == n-1

        l,r = 0, max([w*2 for _,_,w,_ in edges])
        while l < r:
            mid = l + (r-l+1) // 2
            if form_mst(mid):
                l = mid
            else:
                r = mid - 1
        return l
