class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # graph matrix + bfs
        # time O(m*n), space O(m*n)
        m = len(grid)
        n = len(grid[0])

        
        res = 0
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        visit = [[False] * n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                area = 0
                if grid[i][j] == 1 and not visit[i][j]:
                    q.append((i,j))
                    visit[i][j] = True
                
                while q:
                    for _ in range(len(q)):
                        x,y = q.popleft()
                        area += 1
                        for dx,dy in dirs:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and not visit[nx][ny]:
                                q.append((nx,ny))
                                visit[nx][ny] = True
                
                res = max(res, area)
        return res