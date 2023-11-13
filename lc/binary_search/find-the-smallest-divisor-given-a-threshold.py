from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def condition(mid: int) -> bool:

            return sum((n-1) // mid + 1 for n in nums) <= threshold

        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left


s = Solution()
print(s.smallestDivisor([1, 2, 5, 9], 6))
print(s.smallestDivisor([44, 22, 33, 11, 1], 5))
