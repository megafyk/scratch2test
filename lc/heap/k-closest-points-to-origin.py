class Solution:
    import random

    def quickselect(self, arr, l, h, k):
        if l == h:
            return l
        i, j = l, h
        pivot_idx = random.randint(l, h)
        pivot = (
            arr[pivot_idx][0] * arr[pivot_idx][0]
            + arr[pivot_idx][1] * arr[pivot_idx][1]
        )
        while i < j:
            while arr[i][0] * arr[i][0] + arr[i][1] * arr[i][1] < pivot:
                i += 1
            while arr[j][0] * arr[j][0] + arr[j][1] * arr[j][1] > pivot:
                j -= 1
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

        if (arr[j][0] * arr[j][0] + arr[j][1] * arr[j][1]) > pivot:
            j -= 1

        if k <= j - l + 1:
            return self.quickselect(arr, l, j, k)
        else:
            return self.quickselect(arr, j + 1, h, k - (j - l + 1))

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        idx = self.quickselect(points, 0, len(points) - 1, k)
        res = []
        for i in range(idx):
            res.append(points[i])
        return res

    # from heapq import *
    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     # complexity O(n), mem O(n)
    #     minheap = [(x*x + y*y, x, y) for x,y in points]
    #     heapify(minheap)
    #     res = []
    #     for _ in range(k):
    #         _, x, y = heappop(minheap)
    #         res.append([x,y])
    #     return res
