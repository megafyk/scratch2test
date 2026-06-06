class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # array
        # time O(n), space O(1)
        n = len(nums)
        left = 0
        s = sum(nums)
        res = [0] * n
        for i in range(n):
            s -= nums[i]
            res[i] = abs(s - left)
            left += nums[i]
        return res
