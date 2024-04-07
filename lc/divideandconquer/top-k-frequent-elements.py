from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        arr = list(cnt.items())
        kth = self.quickselect(0, len(arr)-1, arr, len(arr) - k) # top kth largest element
        return [num for num, freq in arr if freq >= kth[1]]

    def quickselect(self, l, h, arr, k):
        # find kth smallest element in arr
        # 1 element left
        if l == h:
            return arr[l]
        pivot_idx = self.partition(l, h, arr)

        if k == pivot_idx:
            return arr[k]
        elif k < pivot_idx:
            return self.quickselect(l, pivot_idx-1, arr, k)
        else:
            return self.quickselect(pivot_idx +1, h, arr, k)

    def partition(self, l, h, arr):
        i = l
        pivot = arr[h][1]

        for j in range(l, h):
            if arr[j][1] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i+=1
        arr[i], arr[h] = arr[h], arr[i]
        return i


        
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     # complexity O(n)
    #     cnt = Counter(nums)
    #     heap = [(-freq, val) for val, freq in cnt.items()]

    #     heapq.heapify(heap)
        
    #     ans = []
    #     while k > 0:
    #         ans.append(heapq.heappop(heap)[1])
    #         k -= 1
    #     return ans

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     # complexity O(n), mem O
    #     cnt = Counter(nums)

    #     buckets = [[] for _ in range(len(nums) + 1)]

    #     for num, freq in cnt.items():
    #         buckets[freq].append(num)
        
    #     res = []

    #     for bucket in buckets[::-1]:
    #         for num in bucket:
    #             if k > 0:
    #                 res.append(num)
    #                 k-=1
    #             else:
    #                 return res
    #     return res