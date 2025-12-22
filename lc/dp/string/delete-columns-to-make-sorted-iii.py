class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # dp string
        # time O(m*m*n), space O(m)
        n = len(strs)
        m = len(strs[0])
        dp = [1] * m
        longest = 1
        for i in range(1, m):
            for j in range(i):
                valid = True
                for k in range(n):
                    if strs[k][j] > strs[k][i]:
                        valid = False
                        break
                if valid:
                    dp[i] = max(dp[i], dp[j] + 1)
                    longest = max(longest, dp[i])
                        
        return m - longest