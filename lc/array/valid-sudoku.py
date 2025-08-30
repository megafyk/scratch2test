class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # matrix
        # time O(1), space O(1)
        r_set = [0] * 9
        c_set = [0] * 9
        grid_set = [0] * 9
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                grid = (i // 3) * 3 + (j//3)
                val = int(board[i][j])
                if (r_set[i] >> val) & 1 or (c_set[j] >> val) & 1 or (grid_set[grid] >> val) & 1:
                    return False
                r_set[i] |= 1 << val
                c_set[j] |= 1 << val
                grid_set[grid] |= 1 << val
        return True