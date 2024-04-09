import random


class Solution:

    def quickselect(self, nums, l, h, k):
        if l == h:
            return nums[l]

        i, j = l, h
        pivot = nums[random.randint(l, h)]
        while i < j:
            while nums[i] > pivot:
                i += 1
            while nums[j] < pivot:
                j -= 1

            if i >= j:
                break

            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        if nums[j] < pivot:
            j -= 1

        if k <= j - l + 1:
            return self.quickselect(nums, l, j, k)
        else:
            return self.quickselect(nums, j + 1, h, k - (j - l + 1))

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickselect(nums, 0, len(nums) - 1, k)

    # from heapq import *
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     max_heap = [-num for num in nums]
    #     heapify(max_heap)
    #     res = 10001
    #     for _ in range(k):
    #         res = - heappop(max_heap)
    #     return res

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     # complexity O(nlogn), mem O(1)
    #     nums = sorted(nums, reverse=True)
    #     return nums[k-1]
