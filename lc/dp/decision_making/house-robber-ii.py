class Solution:
    def rob(self, nums: List[int]) -> int: 
        # knapsack 0/1
        # time O(N), space O(1)
        def get_mx(nums):
            n = len(nums)
            dp1, dp2 = 0, nums[0]
            for i in range(1, n):
                nw_dp = max(dp2, dp1 + nums[i])
                dp1 = dp2
                dp2 = nw_dp
            return dp2

        n = len(nums)
        if n == 1: return nums[0]
        return max(get_mx(nums[:n-1]), get_mx(nums[1:]))
