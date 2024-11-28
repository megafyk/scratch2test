from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def inbound(x, y):
            return 0 <= x < n and 0 <= y < m

        def backtrack(x, y, index) -> bool:
            if index == len(word):
                return True

            if not inbound(x, y) or board[y][x] != word[index]:
                return False

            original_char = board[y][x]
            board[y][x] = "#"  # Mark the cell as visited

            # Explore adjacent cells
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if backtrack(x + dx, y + dy, index + 1):
                    return True

            # Restore the original character
            board[y][x] = original_char
            return False

        for y in range(m):
            for x in range(n):
                if board[y][x] == word[0] and backtrack(x, y, 0):
                    return True

        return False


s = Solution()
# print(
#     s.exist([
#         ["A", "B", "C", "E"],
#         ["S", "F", "C", "S"],
#         ["A", "D", "E", "E"]],
#         "ABCB")
# )
print(
    s.exist([
        ["A", "B", "C", "E"], 
        ["S", "F", "C", "S"], 
        ["A", "D", "E", "E"]], 
        "EED")
)
# print(s.exist([["a","a"]], "aaa"))
