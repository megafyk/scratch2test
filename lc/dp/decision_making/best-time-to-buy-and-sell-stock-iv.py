class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # dp making decisions
        # complexity: time O(n*k), space O(k)
        n = len(prices)
        buy = [-sys.maxsize] * (k + 1)
        sell = [0] * (k + 1)

        for i in range(n):
            for j in range(1, k + 1):
                if i == 0:
                    buy[j] = -prices[i]
                    sell[j] = 0
                else:
                    buy[j] = max(buy[j], sell[j - 1] - prices[i])
                    sell[j] = max(sell[j], buy[j] + prices[i])
        return sell[-1]
