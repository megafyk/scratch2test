# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        """  """
        if not root:
            return
        stack = deque([root])
        pre_node = None
        while stack:
            node = stack.pop()
            if pre_node:
                pre_node.left = None
                pre_node.right = node
            
            pre_node = node
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
           
