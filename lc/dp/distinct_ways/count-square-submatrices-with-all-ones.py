class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        # dp
        # time O(m*n), space
        m = len(matrix)
        n = len(matrix[0])

        # dp = [[0] * (n+1) for _ in range(m+1)]
        dp = [0] * (n+1)

        sq = 0
        for i in range(1, m+1):
            tmp_dp = [0] * (n+1)
            for j in range(1, n+1):
                if matrix[i-1][j-1] == 1:
                    tmp_dp[j] = min(dp[j], dp[j-1], tmp_dp[j-1]) + 1
                    sq += tmp_dp[j]
            dp = tmp_dp
        return sq
