class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        q = deque()
        visit = set()
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        walls = set([(x, y) for x, y in walls])
        guards = set([(x, y) for x, y in guards])
        for x, y in guards:
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < m
                    and 0 <= ny < n
                    and (nx, ny) not in walls
                    and (nx, ny) not in guards
                    and (nx, ny, dx, dy) not in visit
                ):
                    q.append((nx, ny, dx, dy))
                    visit.add((nx, ny, dx, dy))

        while q:
            x, y, dx, dy = q.popleft()
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < m
                and 0 <= ny < n
                and ((nx, ny) not in walls)
                and ((nx, ny) not in guards)
                and ((nx, ny, dx, dy) not in visit)
            ):
                q.append((nx, ny, dx, dy))
                visit.add((nx, ny, dx, dy))

        visit = set([(x, y) for x, y, _, _ in visit])
        return m * n - len(visit) - len(guards) - len(walls)

class Solution1:

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
