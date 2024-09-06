# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # complexity: time O(n) mem O(n)
        nums = set(nums)
        dummy = pre = ListNode()
        cur = head
        pre.next = cur

        while cur:
            if cur.val in nums:
                pre.next = cur.next
                cur = cur.next
            else:
                pre = cur
                cur = cur.next
        return head if head.val not in nums else dummy.next
