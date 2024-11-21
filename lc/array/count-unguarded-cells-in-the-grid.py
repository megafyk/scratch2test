class Solution:

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # array
        # time O(m*n), space O(m*n)

        grid = [[0] * n for _ in range(m)]
        def mark(guard):
            row = guard[0]
            col = guard[1]
            for i in range(row+1, m):
                if grid[i][col] == -1 or grid[i][col] == -2: break
                grid[i][col] = 1
            for i in range(row-1, -1, -1):
                if grid[i][col] == -1 or grid[i][col] == -2: break
                grid[i][col] = 1
            for j in range(col+1, n):
                if grid[row][j] == -1 or grid[row][j] == -2: break
                grid[row][j] = 1
            for j in range(col-1, -1, -1):
                if grid[row][j] == -1 or grid[row][j] == -2: break
                grid[row][j] = 1

        for guard in guards:
            grid[guard[0]][guard[1]] = -2

        for wall in walls:
            grid[wall[0]][wall[1]] = -1

        for guard in guards:
            mark(guard)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: count += 1

        return count
