# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # complexity O(n), mem O(n)
        arr = []
        s = deque([(root, root.val)])
        while s:
            node, cursum = s.pop()
            if node.left: s.append((node.left, cursum * 10 + node.left.val))
            if node.right: s.append((node.right, cursum * 10 + node.right.val))
            if not node.left and not node.right: arr.append(cursum)
        return sum(arr)