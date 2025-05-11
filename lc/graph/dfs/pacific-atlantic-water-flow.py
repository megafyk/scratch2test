class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs graph matrix
        # time O(m*n), space O(m*n)
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