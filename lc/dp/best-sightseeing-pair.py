class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        mx, dp = values[0], values[0]

        for i in range(1, n):
            dp = max(dp, values[i - 1] + i - 1)
            mx = max(mx, dp + values[i] - i)
        return mx
