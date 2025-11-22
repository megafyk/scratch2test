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

class Solution1:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def check(node, cur):
            if not cur: return True
            if not node or node.val != cur.val: return False
            return check(node.left, cur.next) or check(node.right, cur.next)

        def dfs(node):
            if not node: return False
            if check(node, head):
                return True
            return dfs(node.left) or dfs(node.right)
        return dfs(root)