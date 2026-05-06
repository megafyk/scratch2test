class Solution:
    def rotateTheBox(self, grid: List[List[str]]) -> List[List[str]]:
        # 2 pointers
        # time O(m*n), space O(m*n)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            r = n - 1
            l = r
            while l >= 0:
                if grid[i][l] == "*":
                    l -= 1
                    r = l
                elif grid[i][l] == "#":
                    grid[i][l], grid[i][r] = grid[i][r], grid[i][l]
                    r -= 1
                    l -= 1
                else:
                    l -= 1

        res = [["."] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][m - 1 - i] = grid[i][j]
        return res
