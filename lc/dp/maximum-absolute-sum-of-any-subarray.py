class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # dp prefix sum
        # time O(N), space O(1)
        min_pre, max_pre = 0, 0
        cur = 0
        res = 0
        for n in nums:
            cur += n
            res = max(res, abs(cur - min_pre), abs(cur - max_pre))
            min_pre = min(min_pre, cur)
            max_pre = max(max_pre, cur)
        return res
