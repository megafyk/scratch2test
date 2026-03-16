class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        s = set()
        for i in range(m):
            for j in range(n):
                s.add(grid[i][j])
                for l in range(1, min(m, n)):
                    if i-l >= 0 and j-l >= 0 and j-2*l >= 0 and i + l < m:
                        sum_vertices = grid[i][j] + grid[i-l][j-l] + grid[i][j-2*l] + grid[i+l][j-l]
                        c1 = c2 = c3 = c4 = 0
                        for k in range(1,l):
                            c1 += grid[i-k][j-k]
                            c2 += grid[i-l+k][j-l-k]
                            c3 += grid[i+k][j-2*l+k]
                            c4 += grid[i+l-k][j-l+k]
                        s.add(sum_vertices + c1 + c2 + c3 + c4)
        s = sorted(list(s), reverse=True)
        return s[:3]