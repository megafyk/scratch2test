class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs on graph matrix
        # time O(m*n), space O(m*n) 
        m = len(grid)
        n = len(grid[0])
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        q = deque()
        visit = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                    visit[i][j] = True
        res = 0
        while q:
            for _ in range(len(q)):
                x,y,t = q.popleft()
                for dx,dy in dirs:
                    nx,ny,nt = x + dx, y + dy, t + 1
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and not visit[nx][ny]:
                        grid[nx][ny] = 2
                        res = max(res, nt)
                        q.append((nx,ny,nt))
                        visit[nx][ny] = True

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: return -1
        return res