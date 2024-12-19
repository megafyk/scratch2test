class Solution:
    def lcs(self, s1, s2):
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

    def minInsertions(self, s: str) -> int:
        # dp string longest common subsequence lcs
        # time O(n^2), space O(n^2)
        return len(s) - self.lcs(s, s[::-1])
