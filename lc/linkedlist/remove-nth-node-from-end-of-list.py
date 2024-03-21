# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = slow = ListNode(-1, head)
        fast = head
        distance_slow_fast = 0

        while distance_slow_fast < n:
            fast = fast.next
            distance_slow_fast += 1

        while fast:
            fast = fast.next
            slow = slow.next

        tmp = slow.next
        slow.next = tmp.next

        # remove head if n == number of nodes in linkedlist
        if slow.val == -1:
            return slow.next

        return head
