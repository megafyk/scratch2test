"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

 
class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return node

        q = deque()
        q.append(node)
        clone_nodes = {node.val: Node(val=node.val, neighbors=[])}

        while q:
            curr_node = q.popleft()
            curr_clone_node = clone_nodes[curr_node.val]

            for neighbor in curr_node.neighbors:
                if neighbor.val not in clone_nodes:
                    clone_nodes[neighbor.val] = Node(val=neighbor.val, neighbors=[])
                    q.append(neighbor)
                curr_clone_node.neighbors.append(clone_nodes[neighbor.val])

        return clone_nodes[node.val]
