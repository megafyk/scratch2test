class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp 0/1 knapsack
        # complexity: time O(o*m*n), mem O(m*n)
        cnt = []
        for num in strs:
            zeros, ones = 0, 0
            for ch in num:
                if ch == "0":
                    zeros += 1
                else:
                    ones += 1
            cnt.append((zeros, ones))
        o = len(strs)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for p in range(1, o + 1):
            zeros, ones = cnt[p - 1]
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])
        return dp[-1][-1]
