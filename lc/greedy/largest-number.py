from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # complexity O(n^2), mem O(1)
        # n = len(nums)
        # for i in range(n-1):
        #     for j in range(n-i-1):
        #         if int(str(nums[j]) + str(nums[j+1])) < int(str(nums[j+1]) + str(nums[j])):
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        # return str(int(''.join(map(str, nums))))
        # complexity O(nlogn), mem O(1)
        def compare(x, y):
            return 1 if int(x + y) < int(y + x) else -1

        nums = list(map(str, nums))
        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(map(str, nums))))
