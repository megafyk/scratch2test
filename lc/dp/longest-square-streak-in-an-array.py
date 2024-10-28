class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # dp
        # time O(nlogn), space O(n)
        nums = sorted(nums, reverse=True)
        dp = {}
        mx = 0
        for num in nums:
            if num not in dp:
                dp[num] = 1
                nxt = num ** 2
                if nxt in dp:
                    dp[num] += dp[nxt]
                mx = max(mx, dp[num])
        return mx if mx != 1 else -1
