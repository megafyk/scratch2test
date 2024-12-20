# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # bfs tree traversal
        # time O(n), space O(n)
        q = deque([root])
        res = root.val
        while q:
            res = q[0].val
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
        return res

    # def dfs(self, root, depth):
    #     if not root: return None, -1
    #     l,dl = self.dfs(root.left, depth+1)
    #     r,dr = self.dfs(root.right, depth+1)
    #     cur, curd = root, depth
    #     if curd < dl: cur, curd = l,dl
    #     if curd < dr: cur, curd = r,dr
    #     return cur,curd

    # def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    #     cur, _ = self.dfs(root, 0)
    #     return cur.val
