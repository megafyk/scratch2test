class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        sumin = defaultdict(int)
        sumout = defaultdict(int)
        cnt = defaultdict(int)

        def dfs_in(i, par):
            cnt[i] = 1
            for j in adj[i]:
                if j != par:
                    dfs_in(j, i)
                    cnt[i] += cnt[j]
                    sumin[i] += sumin[j] + cnt[j]

        def dfs_out(i, par):
            for j in adj[i]:
                if j != par:
                    sumout[j] = sumout[i] + (sumin[i] - sumin[j] - cnt[j]) + (n-cnt[j])
                    dfs_out(j, i)

        dfs_in(0, -1)
        dfs_out(0, -1)

        res = []
        for i in range(n):
            res.append(sumin[i] + sumout[i])

        return res
