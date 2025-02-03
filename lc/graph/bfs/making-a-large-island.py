class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # graph bfs + hashtable
        # time O(m*n), space O(m*n)
        m = len(grid)
        n = len(grid[0])
        visit = set()
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        # precompute
        def get_area(r,c,island_num):
            q = deque([(r,c)])
            grid[r][c] = island_num
            visit.add((r,c))
            area = 1
            while q:
                x,y = q.popleft()
                for dx,dy in dirs:
                    nw_x,nw_y = x+dx,y+dy
                    if 0 <= nw_x < m and 0 <= nw_y < n and (nw_x,nw_y) not in visit and grid[nw_x][nw_y]:
                        visit.add((nw_x,nw_y))
                        grid[nw_x][nw_y] = island_num
                        q.append((nw_x,nw_y))
                        area += 1
            return area


        island_num = 2
        hm = {0:0}
        for r in range(m):
            for c in range(n):
                if grid[r][c] and (r,c) not in visit:
                    visit.add((r,c))
                    hm[island_num] = get_area(r,c,island_num)
                    island_num += 1

        res = max(hm.values())
        # apply operation each 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    cur_area = 1
                    adj_island = set()
                    for dx,dy in dirs:
                        nw_x,nw_y = r+dx,c+dy
                        if 0 <= nw_x < m and 0 <= nw_y < n:
                            island_num = grid[nw_x][nw_y]
                            if island_num not in adj_island:
                                adj_island.add(island_num)
                                cur_area += hm[island_num]
                    res = max(res, cur_area)
        return res
