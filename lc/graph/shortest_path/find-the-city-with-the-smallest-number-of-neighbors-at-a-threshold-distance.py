class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        # dp floyd warshall find shortest dist from u -> v
        # complexity: time O(n^3), mem O(n^2)
        inf = 10**9 + 7
        dp = [[inf] * n for _ in range(n)]

        for u, v, w in edges:
            dp[u][v] = w
            dp[v][u] = w
        for i in range(n):
            dp[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        res = 0
        mi = n
        for i in range(n):
            tmp = [n for n in dp[i] if n <= distanceThreshold]
            if len(tmp) < mi:
                mi = len(tmp)
                res = i
            elif len(tmp) == mi:
                res = max(res, i)
        return res
