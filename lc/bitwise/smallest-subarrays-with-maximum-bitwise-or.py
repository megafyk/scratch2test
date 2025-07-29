class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # bit
        # time O(n), space O(1)
        n = len(nums)
        last_pos = [-1] * 32 # last idx of bit j
        res = [1] * n
        for i in range(n-1, -1, -1):
            for j in range(32):
                if (nums[i] >> j) & 1:
                    last_pos[j] = i
            res[i] = max(res[i], max(last_pos)-i+1)
        return res