# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        # tree
        # time O(N), space O(N)
        self.s = {0}
        q = deque([root])
        root.val = 0

        while q:
            node = q.popleft()
            if node.left:
                l = node.val * 2 + 1
                node.left.val = l
                q.append(node.left)
                self.s.add(l)
            if node.right:
                r = node.val * 2 + 2
                node.right.val = r
                q.append(node.right)
                self.s.add(r)

    def find(self, target: int) -> bool:
        return target in self.s


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
