class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = res = streak = 0
        for num in nums:
            if mx < num:
                mx = num
                res = streak = 0
            if mx == num: streak += 1
            else: streak = 0
            res = max(res, streak)
        return res
