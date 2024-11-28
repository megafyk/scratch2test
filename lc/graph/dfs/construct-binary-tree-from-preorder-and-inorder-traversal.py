# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
    

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_idx_inorder = inorder.index(preorder[0]) 

        left = self.buildTree(preorder[1:root_idx_inorder+1], inorder[:root_idx_inorder+1])
        right = self.buildTree(preorder[root_idx_inorder+1:], inorder[root_idx_inorder+1:])

        return TreeNode(preorder[0], left, right)