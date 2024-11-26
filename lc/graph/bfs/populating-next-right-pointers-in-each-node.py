from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        queue = []
        prev = None
        prev_level = None
        queue.append((root, 0))

        while queue:
            node, level = queue.pop(0)
            if prev and level == prev_level:
                prev.next = node
            prev = node
            prev_level = level
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return root
    
