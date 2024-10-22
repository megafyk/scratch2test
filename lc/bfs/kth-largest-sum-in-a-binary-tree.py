# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # bfs + heap
        # time O(n), space O(n)
        pq = []
        q = deque([(root, 1)])
        cur_lv = 0
        cur_sum = 0
        while q:
            node, lv = q.popleft()
            if lv != cur_lv:
                if cur_lv != 0:
                    heappush(pq, -cur_sum)
                cur_lv = lv
                cur_sum = 0
            cur_sum += node.val
            if node.left: q.append((node.left, lv+1))
            if node.right: q.append((node.right, lv+1))
        heappush(pq, -cur_sum)
        mx_sum = 0
        if k > cur_lv: return -1
        for _ in range(k):
            mx_sum = -heappop(pq)
        return mx_sum