from heapq import *


class Solution:
    
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

    # def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
    #     # priority queue
    #     # complexity: time O(n^2logn), mem O(n)
    #     mod = 10 ** 9 + 7
    #     pq = []
    #     for i in range(n):
    #         heappush(pq, (nums[i], i))
    #     ans = 0
    #     for i in range(1, right+1):
    #         subsum, idx = heappop(pq)
            
    #         if i >= left:
    #             ans += subsum
            
    #         if idx < n-1:
    #             subsum += nums[idx+1]
    #             heappush(pq, (subsum, idx+1))

    #     return ans % mod

    # def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
    #     # brute force
    #     # complexity: time O(n^2logn), mem O(n^2)
    #     mod = 10 ** 9 + 7 
    #     nw_arr = []
    #     for i in range(n):
    #         nw_arr.append(nums[i])
    #         for j in range(i+1, n):
    #             nw_arr.append(nw_arr[-1] + nums[j])

    #     nw_arr = sorted(nw_arr)
    #     return sum(nw_arr[left-1: right]) % mod
