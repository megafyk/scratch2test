# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        # time O(n), space O(n)
        if not root: return []
        q = deque([root])
        res = []
        while q:
            mx_row = -sys.maxsize
            for i in range(len(q)):
                node = q.popleft()
                mx_row = max(mx_row, node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(mx_row)
        return res
