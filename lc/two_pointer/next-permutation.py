from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = -1
        # find item that break descending order from right to left
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                idx = i
                break
        # swap with near higher with idx item from right to left
        if idx != -1:
            for i in range(len(nums) - 1, idx - 1, -1):
                if nums[idx] < nums[i]:
                    nums[idx], nums[i] = nums[i], nums[idx]
                    break
        # swap element from idx item + 1
        left = idx + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


s = Solution()
t = [1, 2, 3]
t = [1, 2, 4, 9, 5, 8, 7, 6]
s.nextPermutation(t)
print(t)
