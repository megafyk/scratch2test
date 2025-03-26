class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # sorting + prefix sum
        # time O(NlogN), space O(N)
        arr = []
        m = len(grid)
        n = len(grid[0])
        mod = grid[0][0] % x

        for i in range(m):
            for j in range(n):
                if grid[i][j] % x != mod:
                    return -1
                arr.append(grid[i][j])
        
        arr = sorted(arr)
        total = sum(arr)

        res = sys.maxsize
        prefix = 0
        for i in range(m*n):
            left = arr[i] * i - prefix
            right = total - prefix - (arr[i] * (n*m-i))
            res = min(res, left + right)
            prefix += arr[i]
            
        return res // x
