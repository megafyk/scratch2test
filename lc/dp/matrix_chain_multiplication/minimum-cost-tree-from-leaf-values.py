class Solution:
    def dp(self, arr, i, j, memo):
        if i == j: return (arr[i], 0)
        if (i,j) in memo: return memo[(i,j)]
        max_leaf = 0
        min_par = sys.maxsize
        for k in range(i, j):
            max_left, min_left = self.dp(arr, i, k, memo)
            max_right, min_right = self.dp(arr, k+1, j, memo)
            max_leaf = max(max_leaf, max_left, max_right)
            min_par = min(min_par, max_left * max_right + min_left + min_right)

        memo[(i,j)] = (max_leaf, min_par)
        return max_leaf, min_par

    def mctFromLeafValues(self, arr: List[int]) -> int:
        # dp merging intervals
        # complexity: time O(n^3), mem O(n^2)
        memo = {}
        return self.dp(arr, 0, len(arr)-1, memo)[1]
