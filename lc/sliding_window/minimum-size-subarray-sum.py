class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window
        # time O(N), space O(1)
        if sum(nums) < target: return 0
        i = 0
        N = len(nums)
        cur_sum = 0
        res = N
        for j in range(N):
            cur_sum += nums[j]
            while cur_sum >= target:
                res = min(res, j-i+1)
                cur_sum -= nums[i]
                i += 1
        return res