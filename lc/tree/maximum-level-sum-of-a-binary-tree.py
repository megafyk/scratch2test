# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # bfs
        # time O(n), space O(1)
        mx_sum = -sys.maxsize
        q = deque()
        q.append(root)
        level = 0
        res = 0
        while q:
            cur_sum = 0
            level += 1
            for _ in range(len(q)):
                u = q.popleft()
                cur_sum += u.val
                if u.left:
                    q.append(u.left)
                if u.right:
                    q.append(u.right)
            if cur_sum > mx_sum:
                res = level
                mx_sum = cur_sum
        return res