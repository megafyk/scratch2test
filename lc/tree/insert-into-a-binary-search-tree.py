# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # complexity O(log(n)), mem O(1) 
        new_node = TreeNode(val)
        if not root:
            return new_node
        
        cur, nxt = None, root
        while nxt:
            cur = nxt
            nxt = cur.left if val < cur.val else cur.right

        if val < cur.val:
            cur.left =  new_node
        else:
            cur.right = new_node

        return root