class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window
        # time O(N), space O(1)
        res = 0
        mi = prices[0]
        for i in range(1, len(prices)):
            mi = min(mi, prices[i])
            res = max(res, prices[i] - mi)
        return res