# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, to_delete_set, res):
        if not root:
            return None
        root.left = self.dfs(root.left, to_delete_set, res)
        root.right = self.dfs(root.right, to_delete_set, res)
        if root.val in to_delete_set:
            if root.left:
                res.append(root.left)
            if root.right:
                res.append(root.right)
            return None
        return root

    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        # dfs postorder traversal
        # complexity: time O(n), mem O(n)
        to_delete_set = set(to_delete)
        res = [] if root.val in to_delete_set else [root]
        self.dfs(root, to_delete_set, res)
        return res
