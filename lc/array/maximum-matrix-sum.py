class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # array matrix
        # time O(n), space O(1)
        n = len(matrix)
        abs_total = 0
        abs_min = 10 ** 9 + 7
        nega = 0
        for i in range(n):
            for j in range(n):
                t = abs(matrix[i][j])
                abs_min = min(abs_min, t)
                abs_total += t
                nega += 1 if matrix[i][j] < 0 else 0
        return abs_total if nega % 2 == 0 else abs_total - 2 * abs_min
