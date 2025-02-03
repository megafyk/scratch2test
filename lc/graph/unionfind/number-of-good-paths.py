class Solution:

    def find(self, u, par):
        if u != par[u]:
            par[u] = self.find(par[u], par)
        return par[u]

    def union(self, a, b, par):
        p1 = self.find(a, par)
        p2 = self.find(b, par)

        # already connected 
        if p1 == p2:
            return

        # union
        if p1 < p2:
            par[b] = p1
        else:
            par[a] = p2

    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        # complexity: time O(nlogn), mem O(n)
        n = len(vals)
        res = n
        
        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        
        vals2idx = collections.defaultdict(list)
        for idx, val in enumerate(vals):
            vals2idx[val].append(idx)

        res = 0
        par = [i for i in range(n)]

        for val in sorted(vals2idx.keys()):
            for node in vals2idx[val]:
                for adj in graph[node]:
                    if vals[adj] <= vals[node]:
                        self.union(adj, node, par)
            if val == 2:
                print(par)
            cnt = collections.defaultdict(int)
            for node in vals2idx[val]:
                cnt[self.find(node, par)] += 1
                res += cnt[self.find(node, par)]
              
        return res
