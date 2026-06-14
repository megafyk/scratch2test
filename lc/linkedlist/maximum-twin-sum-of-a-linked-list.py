# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # linked list
        # time O(n), space O(n)
        cur = head
        n = 0

        while cur:
            n += 1
            cur = cur.next
        half = head
        half_cnt = 0

        while half_cnt < n // 2:
            half = half.next
            half_cnt += 1
        prev, cur = None, half

        while cur:
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp
        h1 = head
        h2 = prev
        mx = 0

        while h2:
            mx = max(mx, h1.val + h2.val)
            h1 = h1.next
            h2 = h2.next
        return mx
