class Solution:
    def canWinNim(self, n: int) -> bool:
        return n & 3
        # dp = [True] * (n+1)
        # for i in range(4,n+1):
        #     if dp[i-3] and dp[i-2] and dp[i-1]:
        #         dp[i] = False
        # return dp[-1]


        