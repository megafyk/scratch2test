class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        # dp distinct ways
        # time O(n^2), space O(n)
        n = len(board)
        mod = 10**9+7
        dp = [[-1,0] for _ in range(n)]

        def get_best(prev, cur, t):
            prev_sum = prev[0] + t
            prev_path = prev[1]
            if prev_sum > cur[0]:
                cur = [prev_sum, prev_path]
            elif prev_sum == cur[0]:
                cur[1] = (cur[1] + prev_path) % mod
            return cur

        for i in range(n-1, -1, -1):
            nw_dp = [[-1,0] for _ in range(n)]
            for j in range(n-1, -1, -1):
                # base case
                if (i,j) == (n-1, n-1):
                    nw_dp[j] = [0,1]
                    continue
                if board[i][j] == 'X':
                    continue
                t = 0
                if board[i][j] != 'E' and board[i][j] != 'S':
                    t = int(board[i][j])
                nw_dp[j] = get_best(dp[j], nw_dp[j], t)
                if j < n-1:
                    nw_dp[j] = get_best(nw_dp[j+1], nw_dp[j], t)
                    nw_dp[j] = get_best(dp[j+1], nw_dp[j], t)
            dp = nw_dp
        return dp[0] if dp[0][1] > 0 else [0,0]

class Solution1:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        # brute force (tle O(3^n))
        n = len(board)
        dist = [[[0,0] for _ in range(n)] for _ in range(n)]
        q = deque()
        q.append((n-1,n-1))
        dirs = [(-1,-1),(-1,0), (0,-1)]
        while q:
            x,y = q.popleft()
            for dx,dy in dirs:

                nx,ny = x+dx,y+dy

                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 'X':

                    num = 0
                    if board[nx][ny] != 'E':
                        num = int(board[nx][ny])

                    t = dist[x][y][0] + num

                    if t > dist[nx][ny][0]:
                        dist[nx][ny] = [t, 1]
                        q.append((nx,ny))

                    elif t == dist[nx][ny][0]:
                        dist[nx][ny][1] += 1
                        q.append((nx,ny))
        return dist[0][0]
