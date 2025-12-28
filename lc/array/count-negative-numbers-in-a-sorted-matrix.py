class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # sorted matrix
        # time O(m+n), space O(1)
        n = len(grid[0])
        res = 0
        j = n
        for row in grid:
            while j > 0 and row[j-1] < 0:
                j -= 1
            if j < n and row[j] < 0:
                res += (n-j)
        return res