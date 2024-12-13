class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp kadane's algorithm
        # time O(n), space O(1)
        prefix, suffix = 0,0
        mx = -10 ** 9 + 7
        n = len(nums)
        for i in range(n):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[n-i-1]
            mx = max(mx, prefix, suffix)
        return mx
