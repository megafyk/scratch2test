class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        # sliding window
        # time O(N), space O(1)
        N = len(nums)
        res = 0
        for i in range(1, N-1):
            if nums[i] == (nums[i-1] + nums[i+1]) * 2:
                res += 1
        return res