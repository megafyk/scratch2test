class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None
        self.prv = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.count = 0
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False  
        new_node = Node(value)
        if self.isEmpty():
            self.tail = self.head = new_node
        else:
            new_node.nxt = self.head
            self.head.prv = new_node
            self.head = new_node
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        new_node = Node(value)
        if self.isEmpty():
            self.tail = self.head = new_node
        else:
            self.tail.nxt = new_node
            new_node.prv = self.tail
            self.tail = new_node
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        if self.count == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.nxt
            self.head.prv = None
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        if self.count == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prv
            self.tail.nxt = None
            
        self.count -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.head.val

    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.k == self.count


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
