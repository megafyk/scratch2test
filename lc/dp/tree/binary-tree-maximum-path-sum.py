# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.max_path = -sys.maxsize

    def dfs(self, root):
        if not root: return 0
        max_root_left = max(self.dfs(root.left), 0) # consider only positive value
        max_root_right = max(self.dfs(root.right), 0)
        cur_max = root.val + max_root_left + max_root_right # go left -> root -> right
        self.max_path = max(self.max_path, cur_max)
        return root.val + max(max_root_left, max_root_right) # go up

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # dp tree
        # time O(n), space O(h)
        self.dfs(root)
        return self.max_path
