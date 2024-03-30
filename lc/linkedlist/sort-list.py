# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # complexity O(n^2), mem O(1)
        # cur2 = None
        # while cur2 != head:
        #     cur1 = head
        #     while cur1 != cur2 and cur1.next != cur2:
        #         if cur1.val > cur1.next.val:
        #             cur1.val, cur1.next.val = cur1.next.val, cur1.val
        #         cur1 = cur1.next
        #     cur2 = cur1
        # return head

        # complexity O(nlogn), mem O(n) because recursion stack

        if not head or not head.next:
            return head

        slow = fast = head
        prev = ListNode()
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        left = self.sortList(head)
        right = self.sortList(slow)

        cur = new_head = ListNode()

        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next

        cur.next = left if left else right

        return new_head.next
