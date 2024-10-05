class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # time O(n), space O(1)
        n = len(nums)
        i, j = 0, 0
        while j < n:
            if nums[i] == 0:
                for t in range(j, n):
                    if nums[t] != 0:
                        break
                nums[i], nums[t] = nums[t], nums[i]
                j = t
            i += 1
            j += 1
