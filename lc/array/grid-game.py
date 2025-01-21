class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # prefix sum
        # time O(n), space O(n)
        m = 2
        n = len(grid[0])
        prefix_r1 = [0] * n
        prefix_r2 = [0] * n
        for i in range(n):
            prefix_r1[i] = grid[0][i] + (prefix_r1[i-1] if i > 0 else 0)
            prefix_r2[i] = grid[1][i] + (prefix_r2[i-1] if i > 0 else 0)
        print(prefix_r1, prefix_r2)
        res = sys.maxsize
        for i in range(n):
            top_right = prefix_r1[-1] - prefix_r1[i]
            bottom_left = prefix_r2[i-1] if i > 0 else 0
            rb2 = max(top_right, bottom_left)
            res = min(res, rb2)

        
        return res