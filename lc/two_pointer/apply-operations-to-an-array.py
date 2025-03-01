class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # two pointer
        # time O(n), space O(1)
        n = len(nums)
        non_zero_idx = 0
        for i in range(n):
            if i < len(nums) - 1 and nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            if nums[i] != 0:
                nums[non_zero_idx], nums[i] = nums[i], nums[non_zero_idx]
                non_zero_idx += 1

        return nums