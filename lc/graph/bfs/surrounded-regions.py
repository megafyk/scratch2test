from typing import List
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        q = deque()
        s = set()

        for x in range(m):
            if board[0][x] == "O":
                q.append((x, 0))
            if board[n - 1][x] == "O":
                q.append((x, n - 1))

        for y in range(1, n - 1):
            if board[y][0] == "O":
                q.append((0, y))
            if board[y][m - 1] == "O":
                q.append((m - 1, y))

        def inbound(x, y):
            return 0 <= x < m and 0 <= y < n

        # bfs find all "O" 4 direction-nodes
        while q:
            x, y = q.popleft()
            s.add((x, y)) # visited "O" node

            for xx, yy in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
                if inbound(xx, yy) and board[yy][xx] == "O" and (xx, yy) not in s:
                    q.append((xx, yy))
            
            
        for x in range(m):
            for y in range(n):
                if (x, y) not in s:
                    board[y][x] = "X"


s = Solution()

board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]

# board = [["O", "O"], ["O", "O"]]
s.solve(board)
print(board)
