class Solution:

    def idx_min_row(self, arr):
        idx = 0
        for i in range(len(arr)):
            idx = i if arr[i] < arr[idx] else idx
        return idx

    def max_col(self, matrix, j):
        mx = matrix[0][j]
        for i in range(len(matrix)):
            mx = max(mx, matrix[i][j])
        return mx

    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # complexity: time O(n*m), mem O(1)
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            idx_min_row = self.idx_min_row(matrix[i])
            if matrix[i][idx_min_row] == self.max_col(matrix, idx_min_row):
                return [matrix[i][idx_min_row]]
        return []
