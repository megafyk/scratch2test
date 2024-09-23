class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = -sys.maxsize  # buy 1 trans
        buy2 = -sys.maxsize  # buy 2 trans
        sell1 = 0  # sell 1 trans
        sell2 = 0  # sell all trans

        for price in prices:
            buy1 = max(buy1, -price)
            buy2 = max(buy2, sell1 - price)
            sell1 = max(sell1, buy1 + price)
            sell2 = max(sell2, buy2 + price)

        return max(sell1, sell2)
