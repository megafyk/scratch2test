class Solution:
    def check(self, nums: List[int]) -> bool:
        # array rotate
        # time O(n), space O(n)
        n = len(nums)
        x = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                x = i+1
                break
        if x == 0: return True
        nums = nums * 2
        for i in range(x, x + n - 1):
            if nums[i] > nums[i+1]:
                return False

        return True
