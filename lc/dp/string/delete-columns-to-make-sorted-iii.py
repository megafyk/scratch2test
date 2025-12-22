class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # dp string
        # time O(m*m*n), space O(m*n)
        n = len(strs)
        m = len(strs[0])
        dp = [[1] * m for _ in range(n)]
        longest = 1
        for i in range(1, m):
            for j in range(i):
                valid = True
                for k in range(n):
                    if strs[k][j] > strs[k][i]:
                        valid = False
                        break
                if valid:
                    for k in range(n):
                        dp[k][i] = max(dp[k][i], dp[k][j] + 1)
                        longest = max(longest, dp[k][i])
        return m - longest