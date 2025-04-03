class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # prefix sum
        # time O(N), space O(1)
        n = len(nums)
        imax, dmax = 0,0
        res = 0
        for k in range(n):
            res = max(res, dmax * nums[k])
            imax = max(imax, nums[k])
            dmax = max(dmax, imax - nums[k])
        return res