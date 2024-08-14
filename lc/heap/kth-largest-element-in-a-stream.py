from heapq import *


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # complexity
        self.k = k
        self.pq = []
        for i in range(len(nums)):
            heappush(self.pq, nums[i])
            if len(self.pq) > self.k:
                heappop(self.pq)

    def add(self, val: int) -> int:
        heappush(self.pq, val)
        if len(self.pq) > self.k:
            heappop(self.pq)
        return self.pq[0]

    # def __init__(self, k: int, nums: List[int]):
    #     self.k = k - 1
    #     self.nums = nums

    # def partition(self, low, high):
    #     i = low
    #     pivot = self.nums[high]
    #     for j in range(low, high):
    #         if self.nums[j] >= pivot:
    #             self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
    #             i+=1
    #     self.nums[high], self.nums[i] = self.nums[i], self.nums[high]
    #     return i

    # def quickselect(self, low, high):
    #     if low >= high:
    #         return self.nums[low]

    #     pivot_idx = self.partition(low, high)
    #     if pivot_idx == self.k:
    #         return self.nums[pivot_idx]
    #     elif pivot_idx > self.k:
    #         return self.quickselect(low, pivot_idx-1)
    #     else:
    #         return self.quickselect(pivot_idx+1, high)

    # def add(self, val: int) -> int:
    #     self.nums.append(val)
    #     return self.quickselect(0, len(self.nums)-1)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
