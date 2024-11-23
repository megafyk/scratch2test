# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # dp on tree
        # time O(n), space O(h)
        mod = 10 ** 9 + 7
        self.mx = 0
        def dfs_total(node, ntotal):
            if not node: return 0
            res = node.val
            res += dfs_total(node.left, ntotal)
            res += dfs_total(node.right, ntotal)
            ntotal[node] = res
            return res

        def dfs_mx(root, node, ntotal):
            if not node or (not node.left and not node.right): return 0
            dfs_mx(root, node.left, ntotal)
            dfs_mx(root, node.right, ntotal)
            if node.left:
                self.mx = max(self.mx, (ntotal[root] - ntotal[node.left]) * ntotal[node.left])
            if node.right:
                self.mx = max(self.mx, (ntotal[root] - ntotal[node.right]) * ntotal[node.right])

        ntotal = {}
        dfs_total(root, ntotal)
        dfs_mx(root, root, ntotal)
        return self.mx % mod
