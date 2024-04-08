import heapq

class SeatManager:

    def __init__(self, n: int):
        self.pnt = 0
        self.returned = []

    def reserve(self) -> int:

        if not len(self.returned):
            self.pnt += 1
            return self.pnt
        return heapq.heappop(self.returned)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.returned, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)