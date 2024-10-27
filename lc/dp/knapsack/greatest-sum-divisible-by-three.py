class Solution:
    def assign(self, t, dp):
        if t % 3 == 0:
            dp[0] = max(dp[0], t)
        elif t % 3 == 1:
            dp[1] = max(dp[1], t)
        else:
            dp[2] = max(dp[2], t)
    def maxSumDivThree(self, nums: List[int]) -> int:
        # dp mod knapsack 3k,3k+1,3k+2
        # time O(n), space O(1)
        dp = [0] * 3
        for num in nums:
            t0 = dp[0] + num
            t1 = dp[1] + num
            t2 = dp[2] + num
            self.assign(t0, dp)
            self.assign(t1, dp)
            self.assign(t2, dp)
        return dp[0]
