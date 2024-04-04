"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


from typing import List


class Solution:

    def construct(self, grid: List[List[int]]) -> "Node":
        n = len(grid)
        return self.check(grid, 0, 0, n)

    def check(self, grid, row, col, l):
        if l == 1:
            return Node(grid[row][col], True)
        topleft = self.check(grid, row, col, l // 2)
        topright = self.check(grid, row, col + l // 2, l // 2)
        botleft = self.check(grid, row + l // 2, col, l // 2)
        botright = self.check(grid, row + l // 2, col + l // 2, l // 2)

        if all(
            node.isLeaf and node.val == topleft.val
            for node in (topleft, topright, botleft, botright)
        ):
            return Node(topleft.val, True)
        return Node(0, False, topleft, topright, botleft, botright)
