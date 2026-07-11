class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # sliding window
        # time O(n), space O(n)
        par = [i for i in range(n)]
        i = 0
        for j in range(n):
            if nums[j] - nums[i] <= maxDiff:
                par[j] = i
            else:
                if j > 0 and nums[j] - nums[j-1] <= maxDiff:
                    par[j] = i
                else:
                    i = j
        res = []
        for u,v in queries:
            if par[u] == par[v]:
                res.append(True)
            else:
                res.append(False)
        return res

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]

    def find(self, u):
        if self.par[u] != u:
            self.par[u] = self.find(self.par[u])
        return self.par[u]

    def union(self,u,v):
        p1 = self.find(u)
        p2 = self.find(v)
        if p1 == p2:
            return
        if p1 < p2:
            self.par[p2] = p1
        else:
            self.par[p1] = p2

class Solution1:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        i = 0
        uf = UnionFind(n)
        for j in range(n):
            if nums[j] - nums[i] <= maxDiff:
                uf.union(i, j)
            else:
                if j > 0 and nums[j] - nums[j-1] <= maxDiff:
                    uf.union(j-1, j)
                i = j


        res = []
        for u,v in queries:
            if uf.find(u) == uf.find(v):
                res.append(True)
            else:
                res.append(False)
        return res
