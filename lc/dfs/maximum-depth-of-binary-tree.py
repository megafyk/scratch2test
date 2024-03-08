# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def __init__(self):
        self.max_height = -1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def helper(root, height):
            if not root:
                return
            self.max_height = max(self.max_height, height + 1)
            helper(root.left, height + 1)
            helper(root.right, height + 1)

        helper(root, 0)
        return self.max_height
