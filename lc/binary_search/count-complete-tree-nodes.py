# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def exists(self, root, nth):
        cur = root
        for b in bin(nth)[3:]:
            cur = cur.left if b == '0' else cur.right
            if not cur:
                return False
        return True
        
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # complexity time O(logn * logn), mem O(1)
        if not root:
            return 0
        
        h = 0
        cur = root
        while cur.left:
            cur = cur.left
            h += 1
        
        l,r = (1 << h) , (1 << (h+1)) - 1
        # is full complete binary tree
        if self.exists(root, r):
            return r

        while l < r:
            m = l + (r-l) // 2
            if not self.exists(root, m):
                r = m
            else:
                l = m + 1
        return l - 1 # l is minimum node'th which not in tree => l-1