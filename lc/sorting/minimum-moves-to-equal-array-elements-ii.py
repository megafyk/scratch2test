class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # array + sorting -> find median
        # time O(NlogN), space O(1)
        nums = sorted(nums)
        median = len(nums) // 2
        res = 0
        for num in nums:
            res += abs(nums[median] - num)
        
        return res