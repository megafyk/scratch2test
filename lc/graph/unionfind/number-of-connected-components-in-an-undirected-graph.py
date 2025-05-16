from typing import (
    List,
)
from collections import Counter

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
            return
        
        if p1 < p2:
            self.par[p2] = p1
        else:
            self.par[p1] = p2

class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u,v in edges:
            uf.union(u,v)
        s = set()
        for i in range(n):
            s.add(uf.find(i))
        return len(s)