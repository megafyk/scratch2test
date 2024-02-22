# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        m_depth = int('inf')
        
        queue = []
        queue.append((root, 1))
        while queue:
            curr, level = queue.pop(0)
            if not curr.left and not curr.right:
                m_depth = min(m_depth, level)
            else:
                if curr.left: queue.append((curr.left, level+1))
                if curr.right: queue.append((curr.right, level+1))
            
        return m_depth