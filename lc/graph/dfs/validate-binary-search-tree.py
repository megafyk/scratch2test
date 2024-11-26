# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left = root.left
        right = root.right
        
        while left and left.right:
            left = left.right
        while right and right.left:
            right = right.left
        
        if (left and left.val >= root.val) or (right and right.val <= root.val):
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)

        
            