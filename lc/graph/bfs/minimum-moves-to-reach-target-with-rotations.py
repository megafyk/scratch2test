class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        # bfs
        # time O(n^2), space O(n^2)

        n = len(grid)
        q = deque()
        q.append((0,0,0,1,0))
        visit = set()
        visit.add((0,0,0,1))
        while q:
            x1,y1,x2,y2,cnt = q.popleft()
            if (x1,y1,x2,y2) == (n-1,n-2,n-1,n-1):
                return cnt

            if x1 == x2 and y1+1 == y2:
                # move right
                if y2+1 < n and grid[x1][y2+1] == 0 and (x1,y2,x1,y2+1) not in visit:
                    q.append((x1,y2,x1,y2+1,cnt+1))
                    visit.add((x1,y2,x1,y2+1))

                if x1+1 < n and grid[x1+1][y1] == 0 and grid[x1+1][y2] == 0:
                    # move down
                    if (x1+1,y1,x1+1,y2) not in visit:
                        q.append((x1+1,y1,x1+1,y2,cnt+1))
                        visit.add((x1+1,y1,x1+1,y2))

                    # rotate clockwise
                    if (x1,y1,x1+1,y1) not in visit:
                        q.append((x1,y1,x1+1,y1,cnt+1))
                        visit.add((x1,y1,x1+1,y1))

            if y1 == y2 and x1+1 == x2:
                # move down
                if x2 + 1 < n and grid[x2+1][y1] == 0 and (x2,y2,x2+1,y2) not in visit:
                    q.append((x2,y2,x2+1,y2,cnt+1))
                    visit.add((x2,y2,x2+1,y2))

                if y1+1 < n and grid[x1][y1+1] == 0 and grid[x2][y1+1] == 0:
                    # move right
                    if (x1,y1+1,x2,y1+1) not in visit:
                        q.append((x1,y1+1,x2,y1+1,cnt+1))
                        visit.add((x1,y1+1,x2,y1+1))

                    # rotate counter clockwise
                    if (x1,y1,x1,y1+1) not in visit:
                        q.append((x1,y1,x1,y1+1,cnt+1))
                        visit.add((x1,y1,x1,y1+1))

        return -1
