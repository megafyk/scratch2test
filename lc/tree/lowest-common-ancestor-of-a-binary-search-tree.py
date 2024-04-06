# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     # complexity O(h)
    #     if p.val < root.val and q.val < root.val:
    #         return self.lowestCommonAncestor(root.left, p, q)
    #     elif p.val > root.val and q.val > root.val:
    #         return self.lowestCommonAncestor(root.right, p, q)
    #     else:
    #         return root
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # complexity O(h)
        s = deque([root])

        while q:
            node = s.pop()
            if p.val < node.val and q.val < node.val:
                s.append(node.left)
            elif p.val > node.val and q.val > node.val:
                s.append(node.right)
            else:
                return node
        return root