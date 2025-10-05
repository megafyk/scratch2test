class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # bfs
        # time O(m*n), space O(m*n)
        m = len(heights)
        n = len(heights[0])
        
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        def bfs(q, visit):
            while q:
                x,y = q.popleft()
                for dx,dy in dirs:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and not visit[nx][ny] and heights[nx][ny] >= heights[x][y]:
                        visit[nx][ny] = True
                        q.append((nx,ny))
        
        pac = [[False] * n for _ in range(m)]
        q_pac = deque()
        for j in range(n):
            q_pac.append((0, j))
            pac[0][j] = True
        for i in range(m):
            q_pac.append((i,0))
            pac[i][0] = True

        bfs(q_pac, pac)
        
        alt = [[False] * n for _ in range(m)]
        q_alt = deque()
        for j in range(n):
            q_alt.append((m-1, j))
            alt[m-1][j] = True
        for i in range(m):
            q_alt.append((i,n-1))
            alt[i][n-1] = True

        bfs(q_alt, alt)

        res = []
        for i in range(m):
            for j in range(n):
                if pac[i][j] and alt[i][j]:
                    res.append([i,j])
        return res

class Solution1:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs
        m = len(heights)
        n = len(heights[0])

        pacific, alantic = set(), set()
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(visit,x,y):
            visit.add((x,y))
            for dx,dy in dirs:
                nx,ny = x+dx,y+dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visit and heights[x][y] <= heights[nx][ny]:
                    dfs(visit,nx,ny)
        
        for i in range(n):
            dfs(pacific, 0, i)
            dfs(alantic, m-1, i)
        
        for i in range(m):
            dfs(pacific, i, 0)
            dfs(alantic, i, n-1)

        res = []
        for i in range(m):
            for j in range(n):
                if (i,j) in alantic and (i,j) in pacific:
                    res.append([i,j])
        return res