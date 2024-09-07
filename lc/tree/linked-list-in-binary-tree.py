# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, head):
        if not head: return True
        if not node: return False
        if node.val != head.val: return False
        return self.dfs(node.left, head.next) or self.dfs(node.right, head.next)
    
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # complexity: O(n*m), mem O(n)
        if not root: return False
        st = deque([root])
        while st:
            node = st.pop()
            if self.dfs(node, head): return True
            if node.left: st.append(node.left)
            if node.right: st.append(node.right)
        return False


    # def dfs(self, head, node):
    #     if not head: return True
    #     if not node: return False
    #     if node.val != head.val: return False
    #     return self.dfs(head.next, node.left) or self.dfs(head.next, node.right)

    # def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
    #     # complexity: time O(n * m), mem O(n + m)
    #     if not root: return False
    #     return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
