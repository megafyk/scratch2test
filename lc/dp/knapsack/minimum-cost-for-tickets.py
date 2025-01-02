class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # dp knapsack
        # time O(n), space O(n)

        n = days[-1]
        j = 0
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if i < days[j]:
                dp[i] = dp[i - 1]
            else:
                j += 1  # move to next day
                dp[i] = min(
                    dp[max(0, i - 1)] + costs[0],
                    dp[max(0, i - 7)] + costs[1],
                    dp[max(0, i - 30)] + costs[2],
                )
        return dp[-1]
