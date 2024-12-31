class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # complexity: time O(n), mem O(n)
        n = days[-1]
        dp = [0] * (n + 1)
        j = 0
        for i in range(1, n + 1):
            if i < days[j]:
                dp[i] = dp[i - 1]
            else:
                j += 1
                dp[i] = min(
                    costs[0] + dp[i - 1],
                    costs[1] + dp[max(0, i - 7)],
                    costs[2] + dp[max(0, i - 30)],
                )
        return dp[-1]
