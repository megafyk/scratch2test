class Solution:
    def dp(self, i, j, memo):
        if j - i == 0: return 0
        if j - i == 1: return i
        if (i,j) in memo: return memo[(i,j)]
        cost = sys.maxsize
        for k in range(i+1,j):
            cost = min(cost, max(self.dp(i,k-1, memo), self.dp(k+1,j, memo)) + k)
        memo[(i,j)] = cost
        return cost

    def getMoneyAmount(self, n: int) -> int:
        # dp merging interval
        # complexity: time O(n^3), space O(n^2)
        memo = {}
        return self.dp(1, n, memo)
