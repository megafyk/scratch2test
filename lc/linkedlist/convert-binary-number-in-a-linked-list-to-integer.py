# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # time O(n), space O(n)
        bin_str = []
        while head:
            bin_str.append(str(head.val))
            head = head.next
        return int(''.join(bin_str), 2)