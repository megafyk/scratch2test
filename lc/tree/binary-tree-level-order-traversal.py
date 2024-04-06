# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # complexity O(n), mem O(n)
        if not root:
            return root
        
        q = deque([root])
        res = []
        while q:
            size = len(q)
            arr = []
            for i in range(size):
                node = q.popleft()
                arr.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(arr)
        
        return res