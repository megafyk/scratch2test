class Solution:

    def dp(self, n, m, heights, memo):

        if heights in memo:
            return memo[heights]

        start = 0
        min_height = n

        for i in range(len(heights)):
            if heights[i] < min_height:
                min_height = heights[i]
                start = i

        if min_height == n:
            # rectangle is filled with squares
            return 0

        ans = sys.maxsize

        new_heights = list(heights)

        for end in range(start, m):
            if heights[end] == min_height:
                square_edge = end - start + 1
                if square_edge + min_height <= n:
                    new_heights[start : end + 1] = [
                        square_edge + min_height
                    ] * square_edge
                    ans = min(ans, self.dp(n, m, tuple(new_heights), memo) + 1)
            else:
                break

        memo[heights] = ans
        return ans

    def tilingRectangle(self, n: int, m: int) -> int:
        return self.dp(n, m, tuple([0] * m), {})

    # def tilingRectangle(self, n: int, m: int) -> int:
    #     # dp handle special case
    #     # complexity: time O(m*n*n), mem O(m*n)
    #     if (n == 11 and m == 13) or (n == 13 and m == 11): return 6

    #     dp = [[float("inf")] * (n+1) for _ in range(m+1)]

    #     for i in range(1, m+1):
    #         for j in range(1, n+1):
    #             if i == j:
    #                 dp[i][j] = 1
    #             else:
    #                 for k in range(1, i//2+1):
    #                     dp[i][j] = min(dp[i][j], dp[k][j] + dp[i-k][j])
    #                 for k in range(1, j//2+1):
    #                     dp[i][j] = min(dp[i][j], dp[i][k] + dp[i][j-k])
    #     return dp[m][n]
