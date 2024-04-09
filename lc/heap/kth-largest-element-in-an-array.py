import random

class Solution:
    
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