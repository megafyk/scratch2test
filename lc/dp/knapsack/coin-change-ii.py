class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp knapsack bottom up
        # time O(amount*len(coins)), space O(amount)
        dp = [1] + [0] * amount
        for coin in coins:
            nw_dp = [1] + [0] * amount
            for i in range(1, amount+1):
                tmp = dp[i] # not choose coin
                if i >= coin:
                    tmp += nw_dp[i - coin] # choose coin
                nw_dp[i] = tmp
            dp = nw_dp
        return dp[amount]

class Solution1:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp top down
        @cache
        def dfs(a, idx):
            if a == 0: return 1
            if a < 0: return 0
            if idx == len(coins): return 0
            return dfs(a-coins[idx], idx) + dfs(a, idx+1)
        return dfs(amount, 0)