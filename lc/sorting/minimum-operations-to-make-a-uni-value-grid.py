class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])

        arr = []
        mod = grid[0][0] % x
        for i in range(m):
            for j in range(n):
                if grid[i][j] % x != mod:
                    return -1
                arr.append(grid[i][j])
        arr.sort()
        half = (m * n) // 2
        if half == 0:
            return 0
        return (sum(arr[-half:]) - sum(arr[:half])) // x


class Solution1:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        total = 0
        arr = []
        mod = grid[0][0] % x
        for i in range(m):
            for j in range(n):
                if grid[i][j] % x != mod:
                    return -1
                arr.append(grid[i][j])
                total += grid[i][j]
        arr.sort()
        res = inf
        prefix = 0
        for i in range(m * n):
            left = (arr[i] * i) - prefix
            right = total - prefix - (arr[i] * (m * n - i))
            res = min(res, left + right)
            prefix += arr[i]
        return res // x
