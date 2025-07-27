class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # two pointer
        # time O(N), space O(1)
        n = len(nums)
        res = 0
        j = 0 
        for i in range(1, n-1):
            if (nums[i] > nums[j] and nums[i] > nums[i+1]) or (nums[i] < nums[j] and nums[i] < nums[i+1]):
                res += 1
                j = i
        return res