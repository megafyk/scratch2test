class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        # sliding window
        # time O(n), space O(1)
        n = len(prices)
        total, cur_k, gain_k = 0, 0, 0

        for i in range(n):
            total += prices[i] * strategy[i]
            if 0 <= i < k:
                cur_k += prices[i] * strategy[i]
            if k // 2 <= i < k:
                gain_k += prices[i]

        mi = cur_k - gain_k

        for i in range(1, n - k + 1):
            j = i + k - 1
            cur_k -= prices[i - 1] * strategy[i - 1]
            cur_k += prices[j] * strategy[j]
            mid = i + k // 2
            gain_k -= prices[mid - 1]
            gain_k += prices[j]
            mi = min(mi, cur_k - gain_k)

        return max(total - mi, total)
