# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # dp on tree
        # time O(n), space O(h)
        self.mx = 0
        def dfs(node, left, step):
            if node:
                self.mx = max(self.mx, step)
                if left:
                    dfs(node.left, False, step + 1)
                    dfs(node.right, True, 1)
                else:
                    dfs(node.left, False, 1)
                    dfs(node.right, True, step + 1)
        dfs(root, True, 0)
        dfs(root, False, 0)
        return self.mx
