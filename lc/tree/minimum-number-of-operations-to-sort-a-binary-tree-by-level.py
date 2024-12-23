# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        def get_min_swap(arr):
            n = len(arr)
            swap = 0
            arr_sort = sorted(arr)
            pos = {val: idx for idx, val in enumerate(arr)}
            for i in range(n):
                if arr[i] != arr_sort[i]:
                    swap += 1
                    cur_pos = pos[arr_sort[i]]
                    pos[arr[i]] = cur_pos
                    arr[cur_pos] = arr[i]
            return swap

        res = 0
        q = deque([root])
        while q:
            arr = []
            for i in range(len(q)):
                node = q.popleft()
                arr.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res += get_min_swap(arr)
        return res
