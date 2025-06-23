from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return False

        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next


        return False


node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
node2.next = node1
s = Solution()
print(s.hasCycle(node1))
