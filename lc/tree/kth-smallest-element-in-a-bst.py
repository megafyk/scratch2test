# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def __init__(self):
        self.arr = []

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traversal(root, k)
        return self.arr[k-1]

    def traversal(self, root, k):
        if not root or len(self.arr) == k:
            return
        self.traversal(root.left, k)
        self.arr.append(root.val)
        self.traversal(root.right, k)