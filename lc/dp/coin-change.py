class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp
        # complexity: time O(amount * n), mem O(amount)
        if amount == 0:
            return 0
        inf = 10**9 + 7
        dp = [inf] * (amount + 1)
        dp[0] = 0

        for i in range(amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        return dp[-1] if dp[-1] != inf else -1
