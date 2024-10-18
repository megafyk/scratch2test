class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # unbound knapsack
        # time O(n*m), space O(n)
        n = len(coins)
        dp1 = [0] * (amount+1) 
        for j in range(n):
            dp2 = [0] * (amount+1)
            dp2[0] = 1
            for i in range(1, amount + 1):    
                comb = dp1[i]
                if i - coins[j] >= 0:
                    comb = dp1[i] + dp2[i-coins[j]]
                dp2[i] = comb
            dp1 = dp2
        return dp1[-1]

    # def dp(self, amount, coins, i, total, memo):
    #     if total == amount:
    #         return 1
    #     if total > amount:
    #         return 0
    #     if i == len(coins):
    #         return 0
    #     if (i, total) in memo:
    #         return memo[(i, total)]
    #     comb = self.dp(amount, coins, i, total + coins[i], memo) + self.dp(
    #         amount, coins, i + 1, total, memo
    #     )
    #     memo[(i, total)] = comb
    #     return comb

    # def change(self, amount: int, coins: List[int]) -> int:
    #     # unbound knapsack
    #     # time: O(n*m), space O(n*m)
    #     memo = {}
    #     return self.dp(amount, coins, 0, 0, memo)