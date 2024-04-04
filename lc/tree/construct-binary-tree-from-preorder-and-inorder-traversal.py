class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # complexity O(n), mem O(n)
        if not preorder or not inorder:
            return None

        root_inorder_idx = inorder.index(preorder[0])

        left = self.buildTree(preorder[1:root_inorder_idx+1], inorder[:root_inorder_idx+1])
        right = self.buildTree(preorder[root_inorder_idx+1:], inorder[root_inorder_idx+1:])
        
        return TreeNode(preorder[0], left, right)