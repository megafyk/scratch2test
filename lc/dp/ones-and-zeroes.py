class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp knapsack 0/1 bottom up
        # time O(m*n*len(strs)), space O(m*n)
        freq = [Counter(s) for s in strs]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for idx in range(len(strs)):
            z, o = freq[idx]["0"], freq[idx]["1"]
            for i in range(m, z - 1, -1):
                for j in range(n, o - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - z][j - o] + 1)
        return dp[m][n]


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # top down
        freq = [Counter(s) for s in strs]
        @cache
        def dfs(m, n, idx):
            if m < 0 or n < 0:
                return -sys.maxsize
            if idx == len(strs):
                return 0

            res = dfs(m, n, idx + 1)
            res = max(res, dfs(m - freq[idx]["0"], n - freq[idx]["1"], idx + 1) + 1)

            return res

        return dfs(m, n, 0)
