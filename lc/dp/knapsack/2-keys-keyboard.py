class Solution:
    def minSteps(self, n: int) -> int:
        # dp with little math
        # complexity: time O(n), mem O(1)
        dp = [0] * 1001
        dp[0] = 0
        dp[1] = 0
        dp[2] = 2
        dp[3] = 3

        for i in range(4, n + 1):
            dp[i] = i
            for j in range(2, i // 2 + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[i // j] + j)
        return dp[n]
    
class Solution1:
    def minSteps(self, n: int) -> int:
        # bottom-up knapsack 0/1
        # time O(n^2), space O(n^2)
        if n == 1: return 0
        dp = [[sys.maxsize] * (n+1) for _ in range(n+1)]
        dp[1][0] = 0
        for i in range(1, n+1):
            for j in range(n+1):
                if j > 0 and i + j <= n:
                    dp[i+j][j] = min(dp[i+j][i], dp[i][j] + 1)
                if i != j:
                    dp[i][i] = min(dp[i][i], dp[i][j] + 1)
        
        return min(dp[n])

class Solution2:
    def minSteps(self, n: int) -> int:
        # topdown
        # time O(n^2), space O(n^2)
        @cache
        def dfs(cur, copy):
            if cur == n:
                return 0
            if cur > n:
                return sys.maxsize

            res = sys.maxsize
            if copy > 0:
                res = min(res, dfs(cur + copy, copy)  + 1)
            if cur != copy:
                res = min(res, dfs(cur, cur) + 1)
            return res

        return dfs(1, 0)
