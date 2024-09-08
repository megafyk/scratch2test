class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # dp distint ways
        # complexity: time O(m*n*maxMove), mem O(m*n)
        mod = 10 ** 9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        res = 0
        for k in range(maxMove):
            tmp = [[0] * n for _ in range(m)] # next move
            for i in range(m):
                for j in range(n):
                    if i == 0: res = (res + dp[i][j]) % mod
                    if j == 0: res = (res + dp[i][j]) % mod
                    if i == m-1: res = (res + dp[i][j]) % mod
                    if j == n-1: res = (res + dp[i][j]) % mod
                    tmp[i][j] = (
                        (dp[i-1][j] if i > 0 else 0) + 
                        (dp[i][j-1] if j > 0 else 0) +
                        (dp[i+1][j] if i < m - 1 else 0) +
                        (dp[i][j+1] if j < n - 1 else 0)
                    ) % mod
            dp = tmp
        return res
