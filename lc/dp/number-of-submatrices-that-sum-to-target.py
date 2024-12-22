class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # dp with prefixsum + hashmap
        # time O(m^2*n), space O(m*n)
        rows = len(matrix)
        cols = len(matrix[0])
        prefix = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                up = prefix[r-1][c] if r > 0 else 0
                left = prefix[r][c-1] if c > 0 else 0
                up_left = prefix[r-1][c-1] if (r > 0 and c > 0) else 0
                prefix[r][c] = matrix[r][c] + up + left - up_left

        res = 0

        for r1 in range(rows):
            for r2 in range(r1, rows):
                count = defaultdict(int)
                count[0] = 1
                for c in range(cols):
                    cur_sum = prefix[r2][c] - (prefix[r1-1][c] if r1 > 0 else 0)
                    diff = cur_sum - target
                    res += count[diff]
                    count[cur_sum] += 1
        return res
