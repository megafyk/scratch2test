class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # two pointer => dutch's flag
        # time O(N), space O(1)
        red,blue = 0, len(nums) - 1
        for i in range(len(nums)):
            while nums[i] == 2 and i < blue:
                nums[i], nums[blue] = nums[blue], nums[i]
                blue -= 1
            while nums[i] == 0 and i > red:
                nums[i], nums[red] = nums[red], nums[i]
                red += 1