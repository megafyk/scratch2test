from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(can: int):
            count = 0

            for p in piles:
                count += (p-1) // can + 1

            return count <= h

        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2
            if eat(mid):
                right = mid
            else:
                left = mid + 1
        return left 

s = Solution()
print(s.minEatingSpeed([3,6,7,11], 8))
print(s.minEatingSpeed([312884470], 312884469))
