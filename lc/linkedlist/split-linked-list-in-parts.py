# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if not head: return [None] * k
        n = 0
        ans = []
        cur = head
        while cur:
            n += 1
            cur = cur.next
        m = n // k
        remain = n % k
        cuts = [m] * k
        for i in range(k):
            if remain > 0:
                cuts[i] += 1
                remain -= 1

        pre, cur = None, head

        for num in cuts:
            head_of_num = cur
            if head_of_num:
                while cur and num > 0:
                    pre = cur
                    cur = cur.next
                    num -= 1
                pre.next = None
            ans.append(head_of_num)

        return ans
