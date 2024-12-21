class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # tree bottom up dfs
        # time O(V), space O(V)
        adj = defaultdict(list)
        self.res = 0

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(cur, par):
            total = values[cur]

            for child in adj[cur]:
                if child != par:
                    total += dfs(child, cur)

            if total % k == 0:
                self.res += 1

            return total

        dfs(0, -1)

        return self.res
