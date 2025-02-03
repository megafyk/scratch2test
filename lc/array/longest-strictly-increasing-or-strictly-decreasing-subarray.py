class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # array
        # time O(n), space O(1)
        res = 1
        cur_incr = 1
        cur_decr = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                cur_incr += 1
                cur_decr = 1
            elif nums[i-1] > nums[i]:
                cur_decr += 1
                cur_incr = 1
            else:
                cur_incr = cur_decr = 1
            res = max(res, cur_incr, cur_decr)
        return res
        