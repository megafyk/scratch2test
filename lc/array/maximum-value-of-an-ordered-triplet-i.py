class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # prefix sum
        # time O(N), space O(1)
        n = len(nums)
        res,imax,dmax = 0,0,0
        for k in range(n):
            res = max(res, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            imax = max(imax, nums[k])

        return res

    # def maximumTripletValue(self, nums: List[int]) -> int:
    #     # brute force
    #     # time O(N^3), space O(1)
    #     n = len(nums)
    #     res = 0
    #     for i in range(n-2):
    #         for j in range(i+1 , n-1):
    #             for k in range(j+1, n):
    #                 res = max(res, (nums[i] - nums[j]) * nums[k])
    #     return res