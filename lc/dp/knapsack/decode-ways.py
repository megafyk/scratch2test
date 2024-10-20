class Solution:
    def numDecodings(self, s: str) -> int:
        # knapsack
        # time O(n), space O(1)
        if s[0] == "0": return 0
        n = len(s)
        dp0 = dp1 = 1
        for i in range(2, n+1):
            dp = dp1
            num = int(s[i-2] + s[i-1])
            if 10 < num < 20 or 21 <= num <= 26:
                dp += dp0
            elif num == 10 or num == 20:
                dp = dp0
            elif num == 0 or (num > 26 and num % 10 == 0):
                return 0
            dp0 = dp1
            dp1 = dp
        return dp1