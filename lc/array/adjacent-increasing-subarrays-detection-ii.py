class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        # array
        # time O(n), space O(1)
        pre_k = 0
        cur_k = 1
        n = len(nums)
        res = 0
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                cur_k += 1
            else:
                res = max(res, min(pre_k, cur_k), cur_k // 2)
                pre_k = cur_k 
                cur_k = 1

        res = max(res, min(pre_k, cur_k), cur_k // 2)
        return res