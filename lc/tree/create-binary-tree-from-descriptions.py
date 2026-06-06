# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = defaultdict(TreeNode)
        par = defaultdict(int)
        for u, v, left in descriptions:
            if u not in nodes:
                nodes[u] = TreeNode(u)
            if v not in nodes:
                nodes[v] = TreeNode(v)

            if left:
                nodes[u].left = nodes[v]
            else:
                nodes[u].right = nodes[v]

            par[v] = u

        for k in nodes.keys():
            if k not in par:
                return nodes[k]
        return None
