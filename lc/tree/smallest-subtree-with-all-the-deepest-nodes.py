# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # tree dfs
        # time O(N), space O(N)
        def dfs(root):
            if not root: return 0, None
            height_left, left = dfs(root.left)
            height_right, right = dfs(root.right)
            if height_left > height_right: return height_left + 1, left
            elif height_left < height_right: return height_right + 1, right
            return height_left + 1, root
        return dfs(root)[1]