class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # dp -> (values[i]+i) + (values[j]-j) (i<j)
        # time O(n), space O(1)
        n = len(values)
        dp, mx = values[0], values[0]

        for i in range(1, n):
            dp = max(dp, values[i-1] + i-1)
            mx = max(mx, dp + values[i] - i)
        return mx
