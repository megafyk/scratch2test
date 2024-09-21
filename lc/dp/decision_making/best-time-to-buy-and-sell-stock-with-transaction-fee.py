class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # dp decisions making
        # complexity: time O(n), space O(1)
        n = len(prices)
        sell = 0 # max profit last was sell
        buy = -prices[0] # max profit last was buy
        for i in range(1, n):
            buy = max(buy, sell - prices[i])
            sell = max(sell, buy + prices[i] - fee)
        return sell
