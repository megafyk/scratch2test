class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.cnt = n
    
    def find(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return self.par[x]

    def union(self, u,v):
        r1 = self.find(u)
        r2 = self.find(v)
        if r1 != r2:
            self.par[r1] = r2
            self.cnt -= 1

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        # graph union find 
        # time O(n), space O(n)
        N = len(row) // 2
        uf = UnionFind(N)
        for i in range(0, len(row), 2):
            a = row[i] // 2
            b = row[i+1] // 2
            uf.union(a, b)
        return N - uf.cnt


    # def minSwapsCouples(self, row: List[int]) -> int:
    #     # greedy, hashmap
    #     # time O(n), space O(n)
    #     res = 0
    #     hm = {val:idx for idx,val in enumerate(row)}
    #     def swap(i,j):
    #         row[i], row[j] = row[j], row[i]
    #         hm[row[i]] = i
    #         hm[row[j]] = j

    #     for i in range(0, len(row), 2):
    #         first = row[i]
    #         second = first + (1 if row[i] % 2 == 0 else -1)
    #         if second != row[i+1]:
    #             res += 1
    #             swap(i+1, hm[second])

    #     return res