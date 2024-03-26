from typing import List


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
#         # complexity O(n^3)
#         # n = len(nums)
#         # cnt = 0
#         # for i in range(n):
#         #     for j in range(n):
#         #         for k in range(n):
#         #             if (nums[i] & nums[j] & nums[k]) == 0:
#         #                 cnt += 1
#         # return cnt
        cnt = 0
        freq = {}
        for x in nums:
            for y in nums:
                if x & y not in freq:
                    freq[x&y] = 0
                freq[x&y] += 1
        
        for i in nums:
            for j in freq:
                if i & j == 0:
                    cnt += freq[j]
        return cnt