class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # dp knapsack
        # time O(N), space O(N)
        n = len(questions)

        dp = [0] * (n+1)
        for i in range(n-1, -1, -1):
            point, skip = questions[i]
            dp[i] = max(point + dp[min(skip + i + 1, n)], dp[i+1])
        return dp[0]