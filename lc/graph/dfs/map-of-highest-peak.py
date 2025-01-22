class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # bfs on matrix grid
        # time O(m*n), space O(m*n)
        m = len(isWater)
        n = len(isWater[0])
        res = [[-1] * n for _ in range(m)]
        q = deque()
        for r in range(m):
            for c in range(n):
                if isWater[r][c] == 1:
                    q.append((r,c))
                    res[r][c] = 0
        
        cnt = 1
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        while q:
            nxt = len(q)
            for _ in range(nxt):
                x,y = q.popleft()
                for dx,dy in dirs:
                    nwx, nwy = x+dx,y+dy
                    if 0 <= nwx < m and 0 <= nwy < n and res[nwx][nwy] == -1:
                        res[nwx][nwy] = cnt
                        q.append((nwx,nwy))
            cnt += 1

        return res
