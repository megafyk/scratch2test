class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        # brute force,
        # time O((m*n) ^ 2 * min(m,n)), space O(1)
        # optimize use prefix sum
        m = len(grid)
        n = len(grid[0])

        def mg_sq(i,j):
            k = 1
            for l in range(1, min(m-i, n-j)+1):
                base = 0
                for c in range(j, j+l):
                    base += grid[i][c]

                ok = True
                # row sum
                for r in range(i, i+l):
                    s = 0
                    for c in range(j, j+l):
                        s += grid[r][c]
                    if s != base:
                        ok = False
                        break
                if not ok:
                    continue

                # col sum
                for c in range(j, j+l):
                    s = 0
                    for r in range(i, i+l):
                        s += grid[r][c]
                    if s != base:
                        ok = False
                        break
                if not ok:
                    continue

                # diagonal sum
                s1 = s2 = 0
                for d in range(l):
                    s1 += grid[i+d][j+d]
                    s2 += grid[i+d][j+l-1-d]

                if s1 != base or s2 != base:
                    continue
                k = l
            return k

        res = 1
        for i in range(m):
            for j in range(n):
                res = max(res, mg_sq(i,j))
        return res