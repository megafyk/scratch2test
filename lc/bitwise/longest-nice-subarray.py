class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # bitwise + sliding window
        # time O(N), space O(1) 
        res = 0
        i = 0
        mask = 0
        for j in range(len(nums)):
            while mask & nums[j]:
                mask ^= nums[i]
                i += 1
            mask |= nums[j]
            res = max(res, j - i + 1)

        return res
