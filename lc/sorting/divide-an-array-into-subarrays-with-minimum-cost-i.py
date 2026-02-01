class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # sorting
        # time O(n), space O(1)
        n = len(nums)
        a = 51
        b = 52
        
        for i in range(1, n):
            if nums[i] <= a <= b:
                a,b = nums[i], a
            elif a <= nums[i] <= b:
                b = nums[i]
        return nums[0] + a + b