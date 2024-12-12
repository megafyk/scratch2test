class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # dp with hashtable
        # time O(n^2), space O(n^2)
        n = len(arr)
        dp = [{} for _ in range(n)]
        dp[0] = {}
        dp[1] = {arr[0]: 1}
        mx = 1
        for i in range(2, n):
            for j in range(i):
                t = arr[i] - arr[j]
                if t in dp[j]:
                    dp[i][arr[j]] = dp[j][t] + 1
                    mx = max(mx, dp[i][arr[j]] + 1)
                else:
                    dp[i][arr[j]] = 1
        return mx if mx > 1 else 0
