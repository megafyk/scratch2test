# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class BSTIterator:
    # complexity O(n), mem O(n)
    def __init__(self, root: Optional[TreeNode]):
        self.curs = -1
        arr = []
        if root:
            s = deque([root])
            curr = root
            while s:
                while curr.left:
                    curr = curr.left
                    s.append(curr)
                node = s.pop()
                arr.append(node.val)
                if node.right: 
                    curr = node.right
                    s.append(node.right)
        self.arr = arr
        
    def next(self) -> int:
        self.curs += 1
        return self.arr[self.curs]

    def hasNext(self) -> bool:
        return self.curs < len(self.arr) - 1
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()