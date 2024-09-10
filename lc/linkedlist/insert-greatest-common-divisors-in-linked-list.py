# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # complexity: time O(n), mem O(1)
        if not head or not head.next:
            return head
        cur = head
        while cur.next:
            node = ListNode()
            node.val = gcd(cur.val, cur.next.val)
            node.next = cur.next
            cur.next = node
            cur = node.next
        return head
