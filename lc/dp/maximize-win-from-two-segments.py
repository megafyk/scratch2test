class Solution:
    def maximizeWin(self, pos: List[int], k: int) -> int:
        # dp with sliding window
        # time O(n), space O(n)
        n = len(pos)
        dp = [0] * (n+1)
        j = 0
        res = 0
        for i in range(n):
            while pos[i] - k > pos[j]: j+= 1
            dp[i+1] = max(dp[i], i - j + 1)
            res = max(res, i-j+1 + dp[j])
        return res
