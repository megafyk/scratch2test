# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node: return 0,0,sys.maxsize
        l = self.dfs(node.left)
        r = self.dfs(node.right)

        dp1 = l[1] + r[1]
        dp2 = min(min(l[1:]) + r[2], min(r[1:]) + l[2])
        dp3 = 1 + min(l) + min(r)
        return dp1, dp2, dp3

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # dp on tree
        # time O(n), space O(h)
        return min(self.dfs(root)[1:])
