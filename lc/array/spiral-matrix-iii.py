class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        idx = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = 1
        ans = [[rStart, cStart]]
        x, y = rStart, cStart
        count = 0
        while len(ans) < rows * cols:
            dx, dy = dirs[idx]
            for _ in range(steps):
                x, y = x + dx, y + dy
                if 0 <= x < rows and 0 <= y < cols:
                    ans.append([x, y])
            count += 1
            idx = (idx + 1) % 4
            if count % 2 == 0:
                steps += 1
        return ans
