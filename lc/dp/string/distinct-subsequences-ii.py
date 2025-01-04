class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # dp string -> num of sub = 2^n - 1
        # time O(n), space O(n)
        mod = 10**9+7
        prev = {}
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1

        for i in range(1, n+1):
            dup = 0
            if s[i-1] in prev:
                dup = dp[prev[s[i-1]]-1]

            dp[i] = dp[i-1] * 2 - dup

            prev[s[i-1]] = i

        return (dp[-1] - 1) % mod
