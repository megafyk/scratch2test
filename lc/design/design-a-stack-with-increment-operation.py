class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CustomStack:

    def __init__(self, maxSize: int):
        self.maxsize = maxSize
        self.size = 0
        self.head = self.tail = None

    def push(self, x: int) -> None:
        if self.size >= self.maxsize: return
        newnode = Node(x)
        if self.size == 0:
            self.head = self.tail = newnode
        else:     
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
        self.size += 1

    def pop(self) -> int:
        if self.size == 0: return -1
        res = self.tail.value
        # remove tail
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None    
        self.size -= 1
        return res

    def increment(self, k: int, val: int) -> None:
        cur = self.head
        while k > 0:
            k-=1
            if not cur: break
            cur.value += val
            cur = cur.next


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
