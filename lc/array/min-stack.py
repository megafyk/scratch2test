class MinStack:
    # stack array
    # space O(n), time O(1) 
    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        if self.st:
            last = self.st[-1]
            self.st.append((val, min(val, last[1])))
        else:
            self.st = [(val, val)] 

    def pop(self) -> None:
        if self.st:
            self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()