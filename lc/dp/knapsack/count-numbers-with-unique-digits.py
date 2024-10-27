class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # knapsack + math -> dp[i] = 9*9*..*(11-i) + dp(i-1)
        # time O(n), space O(1)
        if n == 0: return 1
        dp = 10
        t = 9
        for i in range(2, n+1):
            t *= (11-i)
            dp += t
        return dp
