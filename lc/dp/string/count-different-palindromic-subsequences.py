class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        # dp string -> count and remove duplicate
        # time O(n^2), space O(n^2)
        mod = 10 ** 9 + 7
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] != s[j]:
                    dp[i][j] = dp[i][j-1] + dp[i+1][j] - dp[i+1][j-1] # count & remove dup
                else:
                    dp[i][j] = dp[i+1][j-1] * 2 # count
                    l,r = i+1, j-1
                    while l <= r and s[l] != s[i]:
                        l += 1
                    while l <= r and s[r] != s[j]:
                        r -= 1

                    if l > r:
                        dp[i][j] += 2
                    elif l == r:
                        dp[i][j] += 1
                    else:
                        dp[i][j] -= dp[l+1][r-1] # dup

        return dp[0][n-1] % mod
