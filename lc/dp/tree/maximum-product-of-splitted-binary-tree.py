# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 10 ** 9 + 7
        node_sum = []
        def dfs(node):
            if not node: return 0
            res = node.val + dfs(node.left) + dfs(node.right)
            node_sum.append(res)
            return res
        root_sum = dfs(root)
        res = 0
        for s in node_sum:
            res = max(res, s * (root_sum - s))
        return res % mod


class Solution1:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 10 ** 9 + 7
        def dfs(node):
            if not node: return 0
            node.val += dfs(node.left) + dfs(node.right)
            return node.val
        
        def dp(node):
            if not node: return 0
            res = node.val * (root.val - node.val)
            return max(res, dp(node.left), dp(node.right))
        
        dfs(root)
        
        return dp(root) % mod
    
class Solution2:
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
