class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp string knapsack bottom up
        # time O(m*n), space O(m*n)
        m = len(s)
        n = len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        for j in range(1,n+1):
            if p[j-1] != "*":
                break
            dp[0][j] = True
        for i in range(1, m+1):
            for j in range(1, n+1):
                match = s[i-1] == p[j-1] or p[j-1] == "?"
                if match:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]

    # def isMatch(self, s: str, p: str) -> bool:
    #     # dp string knapsack topdown
    #     # time O(m*n), space O(m*n)
    #     @cache
    #     def dfs(i, j):
    #         if i >= len(s):
    #             while j < len(p) and p[j] == '*': j += 1
    #             return j == len(p)

    #         if j >= len(p): return False

    #         match = i < len(s) and (s[i] == p[j] or p[j] == "?")

    #         if match:
    #             return dfs(i+1, j+1)
    #         elif p[j] == "*":
    #             not_use_asterisk = dfs(i, j+1)
    #             use_asterisk = dfs(i+1, j)
    #             return not_use_asterisk or use_asterisk

    #         return False

    #     return dfs(0, 0)
