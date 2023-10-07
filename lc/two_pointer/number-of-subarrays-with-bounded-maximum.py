from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans = 0

        start, end = -1, -1

        for i in range(len(nums)):
            if nums[i] > right:
                start = i
            if nums[i] >= left:
                end = i
            print(end - start, end, start)
            ans += (end - start)

        return ans


s = Solution()
print(s.numSubarrayBoundedMax([2, 2, 1, 4, 3], 2, 3))
