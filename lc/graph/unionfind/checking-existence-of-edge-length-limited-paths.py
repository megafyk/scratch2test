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
            return
        if p1 < p2:
            self.par[p2] = p1
        else:
            self.par[p1] = p2


class Solution:
    def distanceLimitedPathsExist(
        self, n: int, edgeList: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        # sorting + unionfind + 2 pointers
        # time O(eloge + qlogq + e + q), space O(n+q)
        edgeList = sorted(edgeList, key=lambda x: x[2])
        queries = [q + [i] for i, q in enumerate(queries)]
        queries = sorted(queries, key=lambda x: x[2])
        i, j = 0, 0

        e = len(edgeList)
        q = len(queries)
        uf = UnionFind(n)

        res = [False] * q
        while j < q:
            while i < e and edgeList[i][2] < queries[j][2]:
                uf.union(edgeList[i][0], edgeList[i][1])
                i += 1
            p1 = uf.find(queries[j][0])
            p2 = uf.find(queries[j][1])
            if p1 == p2:
                res[queries[j][3]] = True
            j += 1
        return res
