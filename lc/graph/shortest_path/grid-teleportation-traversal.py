class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        # bfs + dijkstra
        # time O(m*n + (m*n)log(m*n)), space O(m*n)
        m = len(matrix)
        n = len(matrix[0])
        portal = defaultdict(list)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != "." and matrix[i][j] != "#":
                    portal[matrix[i][j]].append((i, j))

        pq = [(0, 0, 0)]

        dist = [[sys.maxsize] * n for _ in range(m)]
        dist[0][0] = 0

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        portal_used = set()

        while pq:
            move, x, y = heappop(pq)

            if (x, y) == (m - 1, n - 1):
                return move

            if (
                matrix[x][y] != "."
                and matrix[x][y] != "#"
                and matrix[x][y] not in portal_used
            ):
                portal_used.add(matrix[x][y])
                for px, py in portal[matrix[x][y]]: # teleport, same weight => bfs with visited
                    if dist[px][py] > move:
                        dist[px][py] = move
                        heappush(pq, (move, px, py))

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != "#":
                    if dist[nx][ny] > move + 1: # djikstra move with different weight
                        dist[nx][ny] = move + 1
                        heappush(pq, (move + 1, nx, ny))
        return -1
