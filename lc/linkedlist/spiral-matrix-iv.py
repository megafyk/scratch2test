# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # matrix traversal
        # complexity: time O(m*n), mem O(m*n)
        res = [[-1] * n for _ in range(m)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        idx = 0
        x, y = 0,-1
        cur_node = head
        while cur_node:
            dx, dy = dirs[idx]
            tmp_x, tmp_y = x + dx, y + dy
            if tmp_x < 0 or tmp_x >= m or tmp_y < 0 or tmp_y >= n or res[tmp_x][tmp_y] != -1:
                idx = (idx + 1) % 4
                continue
            x, y = tmp_x, tmp_y
            res[x][y] = cur_node.val
            cur_node = cur_node.next
        return res
