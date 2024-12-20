class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp with matrix
        # complexity: time O(m*n), mem O(1)
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] and i >= 1 and j >= 1:
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1
                    ans = max(ans, matrix[i][j])
                elif matrix[i][j]:
                    ans = max(ans, matrix[i][j])
        return ans * ans
