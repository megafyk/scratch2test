class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # dp on array
        # time O(n^2), space O(n^2)
        if len(mines) == n * n:  # All cells are mines
            return 0

        banned = set(map(tuple, mines))

        l = [[0] * n for _ in range(n)]
        r = [[0] * n for _ in range(n)]
        u = [[0] * n for _ in range(n)]
        d = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if (i, j) not in banned:
                    l[i][j] = (l[i][j - 1] + 1) if j > 0 else 1
                    u[i][j] = (u[i - 1][j] + 1) if i > 0 else 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (i, j) not in banned:
                    r[i][j] = (r[i][j + 1] + 1) if j < n - 1 else 1
                    d[i][j] = (d[i + 1][j] + 1) if i < n - 1 else 1

        mx = 0
        for i in range(n):
            for j in range(n):
                if (i, j) not in banned:
                    mx = max(mx, min(l[i][j], r[i][j], u[i][j], d[i][j]))

        return mx
