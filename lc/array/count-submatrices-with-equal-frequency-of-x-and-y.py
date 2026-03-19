class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        sum_x = [0] * n
        sum_y = [0] * n
        for i in range(m):
            cnt_x = cnt_y = 0
            for j in range(n):
                if grid[i][j] == "X":
                    cnt_x += 1
                elif grid[i][j] == "Y":
                    cnt_y += 1
                sum_x[j] += cnt_x
                sum_y[j] += cnt_y
                if sum_x[j] > 0 and sum_x[j] == sum_y[j]:
                    res += 1
        return res