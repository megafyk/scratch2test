from typing import List
import sys

class PersistentUnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.version = [sys.maxsize] * n

    def find(self, x, t=sys.maxsize):
        if self.p[x] == x or self.version[x] >= t:
            return x
        return self.find(self.p[x], t)

    def union(self, a, b, t):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if pa < pb:
            self.version[pb] = t
            self.p[pb] = pa
        else:
            self.version[pa] = t
            self.p[pa] = pb
        return True


class DistanceLimitedPathsExist:
    def __init__(self, n: int, edgeList: List[List[int]]):
        self.puf = PersistentUnionFind(n)
        edgeList.sort(key=lambda x: x[2])
        for u, v, dis in edgeList:
            self.puf.union(u, v, dis)

    def query(self, p: int, q: int, limit: int) -> bool:
        return self.puf.find(p, limit) == self.puf.find(q, limit)
        
def main():
    n = 6
    edges = [[0, 2, 4], [0, 3, 2], [1, 2, 3], [2, 3, 1], [4, 5, 5]]
    query = [[2, 3, 2], [1, 3, 3], [2, 0, 3], [0, 5, 6]]
    s = DistanceLimitedPathsExist(n, edges)
    res = []
    for p,q,limit in query:
        res.append(s.query(p,q,limit))
    print(res)
    print(s.puf.version)


if __name__ == "__main__":
    main()
        