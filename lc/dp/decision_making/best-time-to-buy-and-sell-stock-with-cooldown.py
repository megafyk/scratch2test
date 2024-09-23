class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp making decisions
        # complexity: time O(n), space O(1)
        n = len(prices)
        if n <= 1: return 0
        buy = -prices[0]
        sell = 0
        prev = 0

        for i in range(n):
            tmp = sell
            buy = max(buy, prev - prices[i])
            sell = max(sell, buy + prices[i])
            prev = tmp
        return sell
