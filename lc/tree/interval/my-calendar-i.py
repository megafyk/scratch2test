class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.max_end = end
        self.left = None
        self.right = None


class MyCalendar:

    def __init__(self):
        self.root = None

    def insert(self, cur, node):
        # cur and node are intersect
        if cur.start < node.end and node.start < cur.end:
            return False
        if node.start > cur.start:
            if not cur.right:
                cur.right = node
                cur.max_end = max(cur.max_end, node.max_end)
                return True
            else:
                cur.max_end = max(cur.max_end, node.max_end)
                return self.insert(cur.right, node)
        else:
            if not cur.left:
                cur.left = node
                cur.max_end = max(cur.max_end, node.max_end)
                return True
            else:
                cur.max_end = cur.max_end = max(cur.max_end, node.max_end)
                return self.insert(cur.left, node)

    def book(self, start: int, end: int) -> bool:
        # interval tree
        # complexity: time O(logn), space O(n)
        new_node = Node(start, end)
        if not self.root:
            self.root = new_node
            return True
        return self.insert(self.root, new_node)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
