from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def feasible(day: int):
            bouque = 0
            count = 0
            for d in bloomDay:
                if d <= day:
                    bouque += 1
                    if bouque % k == 0:
                        count += 1
                else:
                    bouque = 0
            return count >= m
        if len(bloomDay) < m * k:
            return -1
        left, right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left

s = Solution()
print(s.minDays([1,10,3,10,2], 3, 1))
print(s.minDays([1,10,3,10,2], 3, 2))
print(s.minDays([7,7,7,7,12,7,7], 2, 3))
