from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        memo = 0
        p1 = l1
        p2 = l2
        l = pre_node = ListNode(p1.val, None)
        while p1 or p2:
            if p1:
                memo += p1.val
                p1 = p1.next
            if p2:
                memo += p2.val
                p2 = p2.next

            new_node = ListNode(memo % 10, None)
            memo = memo // 10
            pre_node.next = new_node
            pre_node = new_node

        if memo != 0:
            pre_node.next = ListNode(memo, None)

        return l.next
