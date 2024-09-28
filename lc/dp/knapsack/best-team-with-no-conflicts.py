from functools import cmp_to_key


class Solution:
    def cmp(self, a, b):
        if a[0] > b[0]: return 1
        if a[0] == b[0]: return 1 if a[1] > b[1] else -1
        return -1

    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # dp knapsack with sort
        # complexity: O(n^2), space O(n)
        n = len(scores)
        arr = [(ages[i], scores[i]) for i in range(n)]
        arr = sorted(arr, key=cmp_to_key(self.cmp))
        dp = [0] * n
        dp[0] = arr[0][1]
        for i in range(1, n):
            dp[i] = arr[i][1]
            for j in range(i):
                if arr[i][1] >= arr[j][1]:
                    dp[i] = max(dp[i], dp[j] + arr[i][1])
        return max(dp)
