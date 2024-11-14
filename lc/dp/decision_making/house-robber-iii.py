# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root: return (0,0)
        pl, npl = self.dfs(root.left)
        pr, npr = self.dfs(root.right)
        proot, nproot = 0, 0
        # pick root
        proot = root.val + max(npl, npr, npl+npr)
        # not pick root
        nproot = max(pl + pr, pl + npr, npl + pr, npl + npr)
        return (proot, nproot)

    def rob(self, root: Optional[TreeNode]) -> int:
        # knapsack on tree
        # time O(n), space O(1)
        return max(self.dfs(root))
