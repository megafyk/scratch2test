# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root: return result
        q = deque()
        q.append((root, 0))

        while q:
            n, level = q.popleft()

            if n.left: q.append((n.left, level+1))
            if n.right: q.append((n.right, level+1))

            result.append(n.val)

            while q:
                tmp_n, tmp_level = q.popleft()
                if tmp_level != level:
                    q.appendleft((tmp_n, tmp_level))
                    break
                else:
                    result[level] = tmp_n.val
                    if tmp_n.left: q.append((tmp_n.left, tmp_level+1))
                    if tmp_n.right: q.append((tmp_n.right, tmp_level+1))
        return result