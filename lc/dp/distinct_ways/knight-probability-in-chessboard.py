class Solution:
    def dp(self, n, k, row, column, memo):
        if k == 0 and 0 <= row < n and 0 <= column < n:
            return 1
        if k == 0 or (row < 0 or row >= n) or (column < 0 or column >= n):
            return 0
        if (k, row, column) in memo:
            return memo[(k, row, column)]
        inboard = 0
        steps = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        for dx, dy in steps:
            inboard += self.dp(n, k - 1, dx + row, dy + column, memo)
        memo[(k, row, column)] = inboard
        return inboard

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # dp distinct ways
        # complexity: time: O(k*row*column), mem O(k*row*column)
        inboard = self.dp(n, k, row, column, {})
        return inboard / (8**k)
