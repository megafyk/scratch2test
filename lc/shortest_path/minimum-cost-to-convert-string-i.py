class Solution:
    def ch2int(self, c):
        return ord(c) - ord("a")

    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        # dp floyd warshall
        # complexity: time O(n), mem O(1)
        inf = float("inf")
        dp = [[inf] * 26 for _ in range(26)]
        for i in range(len(original)):
            u = self.ch2int(original[i])
            v = self.ch2int(changed[i])
            dp[u][v] = min(dp[u][v], cost[i])

        for i in range(len(original)):
            j = self.ch2int(original[i])
            dp[j][j] = 0

        for i in range(len(source)):
            j = self.ch2int(source[i])
            dp[j][j] = 0

        ans = 0

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        ans = 0
        for i in range(len(source)):
            tmp = dp[self.ch2int(source[i])][self.ch2int(target[i])]
            if tmp == inf:
                return -1
            ans += tmp
        return ans
