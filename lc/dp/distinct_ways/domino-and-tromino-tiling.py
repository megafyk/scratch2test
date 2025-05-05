class Solution:
    def numTilings(self, n: int) -> int:
        # dp count distinct ways
        # dp[i] (full) = dp[i-1] (full) + dp[i-2] (full) + dp_top[i-1] (miss top) + dp_bottom[i-1] (miss bot)
        # time O(N), space O(1)
        mod = 10**9 + 7
        dp2, dp1, dp_top, dp_bottom = 1, 1, 0, 0
        for i in range(2, n + 1):
            dp2, dp1, dp_top, dp_bottom = (
                dp2 + dp1 + dp_top + dp_bottom,
                dp2,
                dp_top + dp1,
                dp_bottom + dp1,
            )
        return dp2 % mod

        # return dp[-1]
        # dp,dp_b,dp_t = [0]*(n+1),[0]*(n+1),[0]*(n+1)
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2, n+1):
        #     dp[i] = (dp[i-1] + dp[i-2] + dp_b[i-1] + dp_t[i-1]) % mod
        #     dp_b[i] = dp_b[i-1] + dp[i-2]
        #     dp_t[i] = dp_t[i-1] + dp[i-2]

        # return dp[-1]
