class MyCalendarTwo:

    def __init__(self):
        self.non_overlap = []
        self.overlap = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlap:
            if s < end and start < e:
                return False
        for s, e in self.non_overlap:
            if s < end and start < e:
                self.overlap.append((max(start, s), min(end, e)))
        self.non_overlap.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
