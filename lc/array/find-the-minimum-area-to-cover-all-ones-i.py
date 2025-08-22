class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        a1,b1 = m,n
        a2,b2 = -1,-1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    a1 = min(a1, i)
                    b1 = min(b1, j)
                    a2 = max(a2, i)
                    b2 = max(b2, j)
        
        if a1 == m and b1 == n and a2 == -1 and b2 == -1: return 0
        return (a2 - a1 + 1) * (b2 - b1 +1)