class BrowserHistory:

    def __init__(self, homepage: str):
        self.arr = [homepage]
        self.cur = 0

    def visit(self, url: str) -> None:
        for i in range(len(self.arr)-1, self.cur, -1):
            self.arr.pop()
        self.arr.append(url)
        self.cur += 1

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.arr[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(len(self.arr)-1, self.cur + steps)
        return self.arr[self.cur]


class Node:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.nxt = None

class BrowserHistory1:

    def __init__(self, homepage: str):
        node = Node(homepage)
        self.cur = node

    def visit(self, url: str) -> None:
        node = Node(url)
        nxt = self.cur.nxt
        if nxt:
            nxt.prev = None # detach
        self.cur.nxt = node
        node.prev = self.cur
        self.cur = node

    def back(self, steps: int) -> str:
        for i in range(steps):
            prev = self.cur.prev
            if not prev:
                return self.cur.url
            self.cur = prev
        return self.cur.url

    def forward(self, steps: int) -> str:
        for i in range(steps):
            nxt = self.cur.nxt
            if not nxt:
                return self.cur.url
            self.cur = nxt
        return self.cur.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
