class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # sorting
        # time O(m*nlogn), space O(n)
        m = len(matrix)
        n = len(matrix[0])
        prev_row = [0] * n
        res = 0
        for i in range(m):
            row = [0] * n
            arr = [0] * n
            for j in range(n):
                if matrix[i][j] == 1:
                    row[j] = prev_row[j] + 1
                    arr[j] = row[j]
            arr.sort()
            for j in range(n):
                res = max(res, (n-j) * arr[j])
            prev_row = row
        return res 