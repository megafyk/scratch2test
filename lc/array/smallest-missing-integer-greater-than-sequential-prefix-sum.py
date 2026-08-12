class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # array
        # time O(n), space O(n)
        n = len(nums)
        s = set(nums)
        i = 0
        s_prefix = nums[0]
        for j in range(1, n):
            if nums[j] != nums[j-1] + 1:
                break
            else:
                s_prefix += nums[j]
        while s_prefix in s:
            s_prefix += 1
        return s_prefix
