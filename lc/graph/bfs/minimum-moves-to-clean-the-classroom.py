class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        # graph bfs + greedy (custom visit as state)
        # time O(m*n + m*n*4*2^L), space O(L + m*n*2^L)
        m = len(classroom)
        n = len(classroom[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        little_idx = 0
        little = defaultdict(int)
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == "L":
                    little[(i, j)] = little_idx
                    little_idx += 1
                if classroom[i][j] == "S":
                    start = (i, j)

        full_mask = (1 << little_idx) - 1
        if full_mask == 0:
            return 0

        q = deque([(start[0], start[1], energy, 0, 0)])
        dist = defaultdict(int)
        dist[(start[0], start[1], 0)] = energy  # custom visit state

        while q:
            x, y, e, step, cur_mask = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != "X":
                    nw_e = e - 1

                    nw_mask = cur_mask

                    if classroom[nx][ny] == "L":
                        # remove little
                        idx_little = little[(nx, ny)]
                        nw_mask |= 1 << idx_little

                    if nw_mask == full_mask:
                        return step + 1

                    if classroom[nx][ny] == "R":
                        nw_e = energy

                    nw_state = (nx, ny, nw_mask)
                    if nw_e > 0 and (
                        (nw_state not in dist) or dist[nw_state] < nw_e  # greedy part
                    ):
                        dist[nw_state] = nw_e
                        q.append((nx, ny, nw_e, step + 1, nw_mask))
        return -1
