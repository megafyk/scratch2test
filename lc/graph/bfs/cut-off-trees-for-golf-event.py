class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # matrix + min heap + bfs
        # time O(M*N*(M*N)log(M*N)), space O(M*N)
        pq = []
        M = len(forest)
        N = len(forest[0])
        for i in range(M):
            for j in range(N):
                if forest[i][j] > 1:
                    heappush(pq, (forest[i][j], i,j))
        
        
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        def min_step(start, end):
            # bfs from cur -> nxt == min step from cur -> nxt
            q = deque([start])
            visit = [[False] * N for _ in range(M)]
            visit[start[0]][start[1]] = True

            step = 0
            while q:
                for _ in range(len(q)):
                    x,y = q.popleft()
                    if x == end[0] and y == end[1]: return step
                    for dx,dy in dirs:
                        nx = x + dx
                        ny = y + dy
                        if (0 <= nx < M and 0 <= ny < N) and forest[nx][ny] != 0 and not visit[nx][ny]:
                            q.append((nx,ny))
                            visit[nx][ny] = True
                step += 1
            return -1

        step = 0
        cur = (0,0)
        while pq:
            _,x,y = heappop(pq)
            
            dist = min_step(cur, (x,y))

            if dist == -1: return -1
            step += dist
            cur = x,y

        return step