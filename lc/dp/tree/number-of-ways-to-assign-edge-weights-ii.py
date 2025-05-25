class Solution:
    def assignEdgeWeights(
        self, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        # graph + dfs + lca + binary lifting
        # time O(n log n + q log n), space O(n log n)
        n = len(edges) + 1
        MAX_LOG = (n - 1).bit_length() if n > 1 else 1

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dist = [0] * (n + 1)
        height = [0] * (n + 1)
        dp = [[0] * MAX_LOG for _ in range(n + 1)]

        def dfs(u, p):
            dp[u][0] = p
            for j in range(1, MAX_LOG):
                dp[u][j] = dp[dp[u][j - 1]][j - 1]
            for v in adj[u]:
                if v == p:
                    continue
                dist[v] = dist[u] + 1
                height[v] = height[u] + 1
                dfs(v, u)

        def lca(u, v):
            if height[u] < height[v]:
                u, v = v, u

            k_diff = height[u] - height[v]
            j_lift = 0
            while k_diff > 0:
                if k_diff & 1:
                    u = dp[u][j_lift]
                k_diff >>= 1
                j_lift += 1

            if u == v:
                return u

            for j in range(MAX_LOG - 1, -1, -1):
                if dp[u][j] != dp[v][j]:
                    u = dp[u][j]
                    v = dp[v][j]
            return dp[u][0]

        dfs(1, 0)

        def calc_dist(u, v):
            a = lca(u, v)
            return dist[u] + dist[v] - 2 * dist[a]

        res = [0] * len(queries)
        mod = 10**9 + 7
        for idx, (u, v) in enumerate(queries):
            diff = calc_dist(u, v)
            if diff != 0:
                res[idx] = (2 ** (diff - 1)) % mod
        return res
