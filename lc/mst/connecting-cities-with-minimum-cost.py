from typing import (
    List,
)

from functools import cmp_to_key

class Solution:
    """
    @param n: the number of cities
    @param connections: the connection info between cities
    @return: 
    """

    def cmp_2_conn(self, a, b):
        return 1 if a[2] > b[2] else -1

    def find(self, cur, par):
        if cur != par[cur]:
            par[cur] = self.find(par[cur], par)
        return par[cur]

    def minimum_cost(self, n: int, connections: List[List[int]]) -> int:
        # complexity: time O(nlogn), mem O(n)
        connections = sorted(connections, key=cmp_to_key(self.cmp_2_conn))
        par = [i for i in range(n+1)] 
        cost = 0
        for conn in connections:
            # find
            p1 = self.find(conn[0], par)
            p2 = self.find(conn[1], par)

            if p1 == p2:
                continue
            cost += conn[2]
            # union (connect 2 cities)
            if p1 < p2:
                par[p2] = p1
            else:
                par[p1] = p2
        
        r = self.find(1, par)
        for i in range(1, n+1):
            if self.find(i, par) != r:
                return -1
        return cost