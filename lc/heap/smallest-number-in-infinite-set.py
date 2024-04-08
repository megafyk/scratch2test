import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.pnt = 0
        self.heap = []

    def popSmallest(self) -> int:      
        if self.heap:
            return heapq.heappop(self.heap)
        self.pnt += 1
        return self.pnt
        
    def addBack(self, num: int) -> None:
        if num not in self.heap and num <= self.pnt:
            heapq.heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)