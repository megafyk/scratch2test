class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # dp matrix chain
        # time O(m*n), space O(m*n)
        m = len(matrix)
        n = len(matrix[0])

        self.dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                self.dp[i][j] = matrix[i-1][j-1] + self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        x1,y1 = row1+1, col1+1
        x2,y2 = row2+1, col2+1
        up = self.dp[x1-1][y2]
        left = self.dp[x2][y1-1]

        return self.dp[x2][y2] - up - left + self.dp[x1-1][y1-1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
