class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # bfs in grid + sorting
        # time O(qlogq + q*log(m*n)), space O()
        # first brute force: each query do bfs/dfs to count
        # but time O(q*m*n) -> tle
        # find duplicate works
        # if q[1] > q[0] then count q1 += count q0
        # so do sort q and do bfs
        # but tradition bfs travel every enque
        # so use heap (pq) to optimize
        m = len(grid)
        n = len(grid[0])
        queries_order = [(val, idx) for idx, val in enumerate(queries)]
        queries_order = sorted(queries_order)

        res = [0] * len(queries)
        pq = [(grid[0][0],0,0)]
        prev = 0
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        visit = {(0,0)}
        reward = 0
        # traversal use priority queue
        for val,idx in queries_order:
            while pq and pq[0][0] < val:
                v,x,y = heappop(pq)
                reward += 1
                for dx,dy in dirs:
                    nw_x = x + dx 
                    nw_y = y + dy
                    if 0 <= nw_x < m and 0 <= nw_y < n and (nw_x,nw_y) not in visit:
                        visit.add((nw_x, nw_y))
                        heappush(pq, (grid[nw_x][nw_y], nw_x, nw_y))
            res[idx] = reward
        return res