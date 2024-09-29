class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        mod = 10**9 + 7

        for i in range(len(group)):
            member_needs = group[i]
            profit_earn = profit[i]
            for mem in range(n, member_needs - 1, -1):
                for curr_pro in range(minProfit, -1, -1):
                    new_pro = min(minProfit, curr_pro + profit_earn)
                    dp[mem][new_pro] = (dp[mem][new_pro] + dp[mem - member_needs][curr_pro]) % mod
        return sum(dp[m][minProfit] for m in range(n + 1)) % mod

    # def dp(self, i, m, p, n, minProfit, group, profit, memo):
    #     # dp[i][m][p] -> index, members, current profit
    #     if i == len(group):
    #         return 1 if p >= minProfit else 0
    #     if (i, m, p) in memo:
    #         return memo[(i, m, p)]
    #     # skip crime[i]
    #     res = self.dp(i + 1, m, p, n, minProfit, group, profit, memo)

    #     # do crime[i]
    #     if m + group[i] <= n:
    #         res += self.dp(i + 1, m + group[i], min(p + profit[i], minProfit), n, minProfit, group, profit, memo) # no need to track more i if p >= minProfit

    #     memo[(i, m, p)] = res
    #     return memo[(i, m, p)]

    # def profitableSchemes(
    #     self, n: int, minProfit: int, group: List[int], profit: List[int]
    # ) -> int:
    #     # complexity: time O(n*m*minProfit), space O(n*m*minProfit)
    #     memo = {}
    #     mod = 10**9 + 7
    #     return self.dp(0, 0, 0, n, minProfit, group, profit, memo) % mod
