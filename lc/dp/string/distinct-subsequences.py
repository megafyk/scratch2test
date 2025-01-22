class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp on string
        # time O(m*n), space O(m*n)
        m = len(s)
        n = len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][n] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
        return dp[0][0]


    # def numDistinct(self, s: str, t: str) -> int:
    #     @cache
    #     def dp(i,j):
    #         if j == len(t):
    #             return 1
    #         if i == len(s) and j < len(t):
    #             return 0
                
    #         res = 0
    #         if s[i] == t[j]:
    #             res += dp(i+1,j+1)
    #         res += dp(i+1,j)
    #         return res
    #     return dp(0,0)