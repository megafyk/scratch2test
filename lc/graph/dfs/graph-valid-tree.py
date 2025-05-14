from typing import (
    List,
)
from collections import defaultdict
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # dfs graph detect cycle in undirected graph:
        # time O(V+E), space O(V+E)
        
        if len(edges) != n-1: return False
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(u, par, visit):
            visit.add(u)
            for v in adj[u]:
                if v != par:
                    if v in visit or not dfs(v, u, visit):
                        return False
            return True

        visit = set()
        for u in range(n):
            if u not in visit:
                if not dfs(u, None, visit):
                    return False
        return True