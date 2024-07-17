# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lca(self, root, p, q):
        # lowest common accestor in binary tree
        if not root or root.val == p or root.val == q:
            return root
        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)

        if left and right:
            return root
        elif left:
            return left
        else:
            return right

    def path(self, node, p, path):
        if not node:
            return False
        if node.val == p:
            return True
        path.append("L")
        if self.path(node.left, p, path):
            return True
        path.pop()
        path.append("R")
        if self.path(node.right, p, path):
            return True
        path.pop()
        return False

    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        # dfs
        # complexity: time O(n), mem O(n)
        lca = self.lca(root, startValue, destValue)
        start_path = []
        dest_path = []
        self.path(lca, startValue, start_path)
        self.path(lca, destValue, dest_path)

        start_path = ["U" for _ in start_path]
        return "".join(start_path + dest_path)
