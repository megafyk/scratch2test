# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import *

from heapq import *

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = [(node.val, idx) for idx, node in enumerate(lists) if node]
        heapify(minheap)
        root = prev = None

        while minheap:
            _, idx = heappop(minheap)
            
            if not root:
                root = prev = lists[idx]
            else:
                prev.next = lists[idx]
                prev = lists[idx]
            
            lists[idx] = lists[idx].next
            if lists[idx]:
                heappush(minheap, (lists[idx].val, idx))
            
        return root
