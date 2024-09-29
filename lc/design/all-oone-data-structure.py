class Node:
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()
        self.next = None
        self.prev = None

class AllOne:

    def __init__(self):
        self.ref = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail 
        self.tail.prev = self.head

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def inc(self, key: str) -> None:
        if key in self.ref:
            node = self.ref[key]
            freq = node.freq
            node.keys.remove(key)
            next_node = node.next
            if next_node == self.tail or next_node.freq != freq + 1:
                new_node = Node(freq + 1)
                new_node.keys.add(key)

                new_node.prev = node
                new_node.next = next_node
                node.next = new_node
                next_node.prev = new_node
                self.ref[key] = new_node
            else:
                next_node.keys.add(key)
                self.ref[key] = next_node
            if not node.keys:
                self.remove(node)
        else:
            first = self.head.next
            if first == self.tail or first.freq > 1:
                new_node = Node(1)
                new_node.keys.add(key)
                new_node.prev = self.head
                new_node.next = first
                self.head.next = new_node
                first.prev = new_node
                self.ref[key] = new_node
            else:
                first.keys.add(key)
                self.ref[key] = first
            
                
    def dec(self, key: str) -> None:
        if key not in self.ref:
            return
        node = self.ref[key]
        node.keys.remove(key)
        freq = node.freq
        if freq == 1:
            del self.ref[key]
        else:
            prev = node.prev
            if prev == self.head or prev.freq != freq - 1:
                new_node = Node(freq-1)
                new_node.keys.add(key)
                
                new_node.prev = prev
                new_node.next = node
                prev.next = new_node
                node.prev = new_node
                self.ref[key] = new_node
            else:
                prev.keys.add(key)
                self.ref[key] = prev
        if not node.keys:
            self.remove(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head: return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail: return ""
        return next(iter(self.head.next.keys))
        

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
