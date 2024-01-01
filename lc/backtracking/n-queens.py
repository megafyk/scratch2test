from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        state = [["."] * n for _ in range(n)]

        visited_cols = set()
        visited_diagonals = set()
        visited_anti_diagonals = set()

        def backtrack(row):
            if row == n:
                ans.append(["".join(r) for r in state])
                return
            for col in range(n):
                diagonals_r = row - col
                anti_diagonals_r = row + col
                if (
                    col not in visited_cols
                    and diagonals_r not in visited_diagonals
                    and anti_diagonals_r not in visited_anti_diagonals
                ):
                    state[col][row] = "Q"
                    visited_cols.add(col)
                    visited_diagonals.add(diagonals_r)
                    visited_anti_diagonals.add(anti_diagonals_r)

                    backtrack(row + 1)
                    state[col][row] = "."
                    visited_cols.remove(col)
                    visited_diagonals.remove(diagonals_r)
                    visited_anti_diagonals.remove(anti_diagonals_r)

        backtrack(0)

        return ans


s = Solution()
print(s.solveNQueens(6))
