class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # dp string dp[i][j] is minimum sum to make s1[0:i) == s2[0:j)
        # complexity: time O(n*m), space O(m)
        n = len(s1)
        m = len(s2)
        dp = [0] * (m+1) # dp[i][j] = minimum delete make s1[:i] == s2[:j]

        for j in range(1, m+1):
            dp[j] = ord(s2[j-1]) + dp[j-1]

        for i in range(1, n+1):
            nw_dp = [0] * (m+1)
            nw_dp[0] = ord(s1[i-1]) + dp[0]
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    nw_dp[j] = dp[j-1]
                else:
                    nw_dp[j] = min(ord(s2[j-1]) + nw_dp[j-1], ord(s1[i-1]) + dp[j])
            dp = nw_dp
        return dp[m]
