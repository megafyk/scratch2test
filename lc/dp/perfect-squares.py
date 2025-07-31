class Solution:
    def numSquares(self, n: int) -> int:
        # dp bottom up knapsack 0/1
        # time O(nlogn), space O(n)
        inf = 10**9 + 7
        dp = [inf] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]


class Solution1:
    def numSquares(self, n: int) -> int:
        # dp topdown
        @cache
        def dfs(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            j = 1
            res = sys.maxsize
            while j * j <= i:
                res = min(res, dfs(i - j * j) + 1)
                j += 1
            return res

        return dfs(n)
