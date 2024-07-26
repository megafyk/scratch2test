class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # dp
        # complexity: time O(n*n), mem O(1)
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                mi = matrix[i - 1][j]
                if j - 1 >= 0:
                    mi = min(mi, matrix[i - 1][j - 1])
                if j + 1 < n:
                    mi = min(mi, matrix[i - 1][j + 1])
                matrix[i][j] += mi
        return min(matrix[-1])
