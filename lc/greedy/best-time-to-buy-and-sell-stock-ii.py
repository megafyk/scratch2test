from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0
        for price in prices:
            if price > buy:
                res += price - buy
            buy = price
        return res
