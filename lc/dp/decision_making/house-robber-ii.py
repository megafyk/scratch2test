class Solution:
    def dp(self, nums):
        n = len(nums)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][1] = nums[0]
        for i in range(1, n):
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + nums[i])
            dp[i][0] = dp[i - 1][1]
        return max(dp[-1][0], dp[-1][1])

    def rob(self, nums: List[int]) -> int:
        # knapsack decision making
        # complexity: time O(n), space O(n)
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.dp(nums[1:]), self.dp(nums[: n - 1]))
