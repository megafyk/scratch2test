# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # tree traversal
        # time O(n), space O(n)
        self.idx = 0
        def dfs(depth):
            if not traversal:
                return None, 0
            start = self.idx

            dash_cnt = 0
            while self.idx < len(traversal) and traversal[self.idx] == "-":
                dash_cnt += 1
                self.idx += 1

            if dash_cnt != depth:
                self.idx = start
                return None

            num_start = self.idx
            while self.idx < len(traversal) and traversal[self.idx] != "-":
                self.idx += 1

            if self.idx == num_start:
                self.idx = num_start
                return None

            node = TreeNode()
            node.val = int(traversal[num_start : self.idx])
            node.left = dfs(depth + 1)
            node.right = dfs(depth + 1)
            return node

        return dfs(0)
