class Solution:
    def minOperations(self, nums: list[int]) -> int:
        # time O(n), space O(1)
        n = len(nums)
        res = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                res += nums[i - 1] - nums[i]
        return res
