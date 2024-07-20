class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # greedy choose min between rowSum[i] and colSum[j]
        # complexity: time O(n), mem O(1)
        n = len(rowSum)
        m = len(colSum)

        res = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                res[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= res[i][j]
                colSum[j] -= res[i][j]

        return res
