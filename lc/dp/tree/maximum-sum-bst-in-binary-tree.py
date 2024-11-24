# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        # time O(n), space O(h)
        empty = 0
        is_bst = 1
        is_not_bst = 2
        self.mx = 0

        def dfs(node):
            if not node: return (empty, 0, None, None) # status, total, min_sub_tree, max_sub_tree

            ls,l,ll,lr = dfs(node.left)
            rs,r,rl,rr = dfs(node.right)

            if ((ls == is_bst and lr < node.val) or ls == empty) and ((rs == is_bst and rl > node.val) or rs == empty):

                total = node.val + l + r
                self.mx = max(self.mx, total)
                return (is_bst, total, (ll if ll is not None else node.val), (rr if rr is not None else node.val))

            return (is_not_bst, None, None, None)

        dfs(root)

        return self.mx
