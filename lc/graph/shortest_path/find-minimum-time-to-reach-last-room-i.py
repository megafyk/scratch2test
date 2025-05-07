class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # djikstra
        # time O((M*N)log(M*N)), space O(M*N)
        dirs = [(0,1), (1,0),(0,-1),(-1,0)]
        m = len(moveTime)
        n = len(moveTime[0])
        visit = [[False] * n for _ in range(m)]
        visit[0][0] = True
        pq = [(0,0,0)]
        
        while pq:
            t,x,y = heappop(pq)
            if x == m-1 and y == n - 1:
                return t
            for dx,dy in dirs:
                nx,ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and not visit[nx][ny]:
                    nt = max(t, moveTime[nx][ny]) + 1
                    visit[nx][ny] = True
                    heappush(pq, (nt, nx, ny))

        return -1