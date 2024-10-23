# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # bfs
        # time O(n), space O(n)
        q1 = deque([root])
        q2 = deque([root])

        while q1:
            cur_sum = 0
            for _ in range(len(q1)):
                node = q1.popleft()
                if node.left:
                    cur_sum += node.left.val
                    q1.append(node.left)
                if node.right:
                    cur_sum += node.right.val
                    q1.append(node.right)

            for _ in range(len(q2)):
                node = q2.popleft()
                total = 0
                if node.left: total += node.left.val
                if node.right: total += node.right.val
                if node.left:
                    node.left.val = cur_sum - total
                    q2.append(node.left)
                if node.right:
                    node.right.val = cur_sum - total
                    q2.append(node.right)

        root.val = 0
        return root
