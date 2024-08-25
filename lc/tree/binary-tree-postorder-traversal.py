# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        traversal = []
        st = deque([root])
        while st:
            node = st.pop()
            traversal.append(node.val)
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)
        return traversal[::-1]

    # def dfs(self, visited, node):
    #     if node:
    #         self.dfs(visited, node.left)
    #         self.dfs(visited, node.right)
    #         visited.append(node.val)
    # def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     visited = []
    #     self.dfs(visited, root)
    #     return visited
