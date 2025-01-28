class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        # graph bfs
        # time O(m*n), space O(m*n)
        m = len(grid)
        n = len(grid[0])

        visit = [[False] * n for _ in range(m)]
        
        res = 0
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        def bfs(r,c):
            q = deque([(r,c)])
            visit[r][c] = True
            cnt = 0
            while q:
                x,y = q.popleft()
                cnt += grid[x][y]
                for dx,dy in dirs:
                    nwx,nwy = x+dx,y+dy
                    if 0 <= nwx < m and 0 <= nwy < n and not visit[nwx][nwy] and grid[nwx][nwy] > 0:
                        visit[nwx][nwy] = True
                        q.append((nwx,nwy))
            return cnt
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0 and not visit[r][c]:
                    res = max(res, bfs(r,c))                

        return res