class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # djikstra
        # time O((M*N)log(M*N)), space O(M*N)
        m = len(moveTime)
        n = len(moveTime[0])
        pq = [(0,1,0,0)]
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        visit = [[False] * n for _ in range(m)] 
        while pq:
            t,c,x,y = heappop(pq)
            if x == m-1 and y == n-1:
                return t
            for dx,dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visit[nx][ny]:
                    visit[nx][ny] = True
                    nc = 2 if c == 1 else 1
                    nt = max(t, moveTime[nx][ny]) + c
                    heappush(pq, (nt,nc,nx,ny))
        return -1
