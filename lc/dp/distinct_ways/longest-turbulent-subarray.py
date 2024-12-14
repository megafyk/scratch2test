class Solution:
    def maxTurbulenceSize(self, nums: List[int]) -> int:
        # dp distinct ways
        # time O(n), space O(1)
        n = len(nums)
        dp_u = 1
        dp_d = 1
        mx = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                dp_d = dp_u + 1
                dp_u = 1
            elif nums[i] < nums[i-1]:
                dp_u = dp_d + 1
                dp_d = 1
            else:
                dp_u = 1
                dp_d = 1

            mx = max(mx, dp_u, dp_d)
        return mx
