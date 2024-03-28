from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # complexity = O(n^2), mem O(1)
        # nums = sorted(nums)
        # n = len(nums)
        # while k > 0:
        #     i = 0
        #     nums[i] = -nums[i]
        #     while i < n-1 and nums[i] > nums[i+1]:
        #         nums[i], nums[i+1] = nums[i+1],nums[i]
        #         i+=1
        #     k -=1
        # return sum(nums)
        # complexity = O(nlogn) -> can use counting sort to reduce to O(n), mem O(1)
        nums = sorted(nums)
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 and k > 0:
                k -= 1
                nums[i] = -nums[i]
        nums = sorted(nums)
        if k & 1:
            nums[0] = -nums[0]
        return sum(nums)
