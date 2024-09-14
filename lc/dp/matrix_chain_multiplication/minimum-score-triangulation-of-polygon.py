class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        # dp merging intervals
        # complexity: time O(n^3), mem O(n^2)
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        
        for j in range(2, n):
            for i in range(j-2, -1, -1):
                dp[i][j] = sys.maxsize
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + values[i] * values[j] * values[k])
        return dp[0][-1]

    # def dp(self, values, i, j, memo):
    #     if j - i == 2: return values[i] * values[j] * values[i+1]
    #     if j - i < 2: return 0
    #     if (i, j) in memo: return memo[(i,j)]
    #     score = sys.maxsize
    #     for k in range(i+1, j):
    #         score = min(score, self.dp(values,i,k, memo) + values[i] * values[j] * values[k] + self.dp(values,k,j, memo))
    #     memo[(i,j)] = score
    #     return score

    # def minScoreTriangulation(self, values: List[int]) -> int:
    #     memo = {}
    #     return self.dp(values, 0, len(values)-1, memo)
