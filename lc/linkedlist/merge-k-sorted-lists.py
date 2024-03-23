# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TODO: still got tle
class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        curr = head

        # priority queue use min heap implementation
        heap = [curr]

        def inserth(heap, ele: ListNode):
            heap.append(ele)
            idx_ele = len(heap) - 1
            idx_parent = idx_ele // 2
            while idx_parent > 0 and heap[idx_ele].val < heap[idx_parent].val:
                heap[idx_ele], heap[idx_parent] = heap[idx_parent], heap[idx_ele]
                idx_ele = idx_parent
                idx_parent = idx_ele // 2

        def deleteh(heap) -> ListNode:
            heap[1], heap[-1] = heap[-1], heap[1]
            pop_node = heap.pop()
            idx_tmp = 1
            len_heap = len(heap)
            val_tmp_left = (
                heap[idx_tmp * 2].val if idx_tmp * 2 < len_heap else 10 ^ 4 + 1
            )
            val_tmp_right = (
                heap[idx_tmp * 2 + 1].val if idx_tmp * 2 + 1 < len_heap else 10 ^ 4 + 1
            )

            # rearrange heap
            while idx_tmp < len_heap - 1 and (
                heap[idx_tmp].val > val_tmp_left or heap[idx_tmp].val > val_tmp_right
            ):
                if val_tmp_left < val_tmp_right:
                    heap[idx_tmp], heap[idx_tmp * 2] = heap[idx_tmp * 2], heap[idx_tmp]
                    idx_tmp = idx_tmp * 2
                elif idx_tmp * 2 + 1 < len_heap:
                    heap[idx_tmp], heap[idx_tmp * 2 + 1] = (
                        heap[idx_tmp * 2 + 1],
                        heap[idx_tmp],
                    )
                    idx_tmp = idx_tmp * 2 + 1

                val_tmp_left = (
                    heap[idx_tmp * 2].val if idx_tmp * 2 < len_heap else 10 ^ 4 + 1
                )
                val_tmp_right = (
                    heap[idx_tmp * 2 + 1].val
                    if idx_tmp * 2 + 1 < len_heap
                    else 10 ^ 4 + 1
                )
            return pop_node

        # init heap
        for node in lists:
            if node:
                inserth(heap, node)

        while len(heap) > 1:
            node = deleteh(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                inserth(heap, node.next)

        return head.next
