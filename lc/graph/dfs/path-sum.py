# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import deque
from typing import Optional
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = deque([(root, 0)])
        while stack:
            node, val = stack.pop()
            
            if not node.left and not node.right and val + node.val == targetSum:
                return True
            
            if node.left: 
                stack.append((node.left, val + node.val))

            if node.right: 
                stack.append((node.right, val + node.val))

        return False