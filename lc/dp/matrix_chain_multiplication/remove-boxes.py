class Solution:
    def dp(self, boxes, memo, i, j, k):
        if i > j: return 0
        if i == j: return (k+1)*(k+1)
        if memo[i][j][k] != -1: return memo[i][j][k]
        based = (k+1) * (k+1) + self.dp(boxes, memo, i+1, j, 0)
        mx = based
        for idx in range(i+1, j+1):
            if boxes[idx] == boxes[i]:
                mx = max(mx, self.dp(boxes, memo, i+1, idx-1, 0) + self.dp(boxes, memo, idx, j, k+1))
        memo[i][j][k] = mx
        return mx

    def removeBoxes(self, boxes: List[int]) -> int:
        # dp matrix chain multiplication
        n = len(boxes)
        memo = [[[-1] * n for _ in range(n)] for _ in range(n)]
        return self.dp(boxes, memo, 0, n-1, 0)
