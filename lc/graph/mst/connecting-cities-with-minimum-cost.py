from typing import (
    List,
)

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]

    def find(self, u):
        if u != self.par[u]:
            self.par[u] = self.find(self.par[u])
        return self.par[u]
    def union(self, u, v):
        p1 = self.find(u)
        p2 = self.find(v)
        if p1 != p2:
            self.par[p2] = p1
            return True
        return False

class Solution:
    """
    @param n: the number of cities
    @param connections: the connection info between cities
    @return: 
    """
    def minimum_cost(self, n: int, connections: List[List[int]]) -> int:
        # mst kruskal
        # time O(ElogE), space O(n)
        cnt_edge = 0
        connections.sort(key = lambda x: x[2])
        res = 0
        uf = UnionFind(n)
        for u,v,w in connections:
            if uf.union(u,v):
                cnt_edge += 1
                res += w
            if cnt_edge == n-1:
                return res
        return -1