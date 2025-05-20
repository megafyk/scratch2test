class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # array kadahn's algorithm
        # time O(N), space O(1) 
        n = len(nums)
        mx = mi = nums[0]
        cur_mx = cur_mi = 0
        total = 0
        for i in range(n):
            cur_mx = max(cur_mx + nums[i], nums[i])
            mx = max(mx, cur_mx)
            cur_mi = min(cur_mi + nums[i], nums[i])
            mi = min(mi, cur_mi)

            total += nums[i]

        if total == mi: return mx
        return max(mx, total - mi)
            