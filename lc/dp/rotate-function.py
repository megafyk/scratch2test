class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # dp on array
        # time O(N), space O(1)
        n = len(nums)
        total = 0
        f0 = 0
        for i in range(n):
            total += nums[i]
            f0 += i * nums[i]
        res = f0
        for i in range(n - 1, -1, -1):
            f = f0 - nums[i] * (n - 1) + (total - nums[i])
            f0 = f
            res = max(res, f0)
        return res
