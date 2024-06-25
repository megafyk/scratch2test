# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # dfs use stack. preorder traversal
        # complexity: time O(n), mem O(n)
        if not root:
            return 0
        arr = []
        st = deque([(root, 0)])
        while st:
            node, cur = st.pop()
            cur = cur * 10 + node.val
            if not node.left and not node.right:
                arr.append(cur)
            if node.left:
                st.append((node.left, cur))
            if node.right:
                st.append((node.right, cur))
        return sum(arr)

    # def dfs(self, root, cur):
    #     cur = cur * 10 + root.val
    #     if not root.left and not root.right: self.arr.append(cur)
    #     if root.left: self.dfs(root.left, cur)
    #     if root.right: self.dfs(root.right, cur)

    # def sumNumbers(self, root: Optional[TreeNode]) -> int:
    #     if not root: return 0
    #     self.arr = []
    #     self.dfs(root, 0)
    #     return sum(self.arr)
