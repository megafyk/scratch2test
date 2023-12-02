from typing import List


# use 2 pointer
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # find number break descending order from right to left
        idx = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                idx = i
                break
        # swap with nearest higher than nums[idx]
        if idx != -1:
            for i in range(len(nums) - 1, idx - 1, -1):
                if nums[i] > nums[idx]:
                    nums[i], nums[idx] = nums[idx], nums[i]
                    break
        # swap all element from nums[idx] to end
        left = idx + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


s = Solution()
nums = [1, 2, 3, 4]
s.nextPermutation(nums)
print(nums)
