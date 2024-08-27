"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        stack = deque([root])
        traversal = []
        while stack:
            node = stack.pop()
            traversal.append(node.val)
            for c in node.children:
                if c:
                    stack.append(c)
        return traversal[::-1]
