class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r_set = [0] * 9
        c_set = [0] * 9
        g_set = [0] * 9
        need_fill = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    need_fill.append((i, j))
                else:
                    num = int(board[i][j])
                    g_idx = (i // 3) * 3 + (j // 3)
                    r_set[i] |= 1 << num
                    c_set[j] |= 1 << num
                    g_set[g_idx] |= 1 << num

        def backtrack(idx):
            if idx == len(need_fill):
                return True
            x, y = need_fill[idx]
            for num in range(1, 10):
                g_idx = (x // 3) * 3 + (y // 3)
                if (
                    (r_set[x] >> num) & 1 == 0
                    and (c_set[y] >> num) & 1 == 0
                    and (g_set[g_idx] >> num) & 1 == 0
                ):
                    board[x][y] = str(num)
                    r_set[x] |= 1 << num
                    c_set[y] |= 1 << num
                    g_set[g_idx] |= 1 << num
                    if backtrack(idx + 1):
                        return True
                    board[x][y] = "."

                    r_set[x] -= 1 << num
                    c_set[y] -= 1 << num
                    g_set[g_idx] -= 1 << num

            return False

        backtrack(0)
