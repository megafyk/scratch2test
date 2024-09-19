class Solution:
    def rob(self, nums: List[int]) -> int:
        # decision making, dp[i][j] -> j=1 mean i house is robbed
        # complexity: time O(n), mem O(n)
        n = len(nums)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][1] = nums[0]
        for i in range(1, n):
            dp[i][1] = max(dp[i-1][0] + nums[i], dp[i-1][1])
            dp[i][0] = dp[i-1][1]
        return max(dp[-1][0], dp[-1][1])
