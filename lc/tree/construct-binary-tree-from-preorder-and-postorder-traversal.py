# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
    # tree traversal
    # time O(N), space O(N)
        n = len(preorder)
        if n == 0:
            return None
        root = TreeNode(val=preorder[0])
        if n == 1:
            return root
        
        left_root_val = preorder[1]
        left_size = postorder.index(left_root_val) + 1


        root.left = self.constructFromPrePost(
            preorder[1:1+left_size], postorder[:left_size]
        )

        root.right = self.constructFromPrePost(
            preorder[left_size+1:], postorder[left_size:n-1]
        )

        return root
