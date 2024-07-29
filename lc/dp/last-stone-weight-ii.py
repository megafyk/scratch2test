class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # dp 0/1 knapsack
        # complexity: time O(ns), mem O(ns)
        n = len(stones)
        s = sum(stones)
        target = s // 2
        # stones and target
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if stones[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(
                        dp[i - 1][j], stones[i - 1] + dp[i - 1][j - stones[i - 1]]
                    )
        return s - 2 * dp[-1][target]
