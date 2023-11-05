from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        
        def feasible(cap: int):
            total = 0
            d = 1
            for w in weights:
                total += w
                if total > cap:
                    total = w
                    d += 1
                    if d > days:
                        return False
            return True

        left, right = max(weights), sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left
    
s = Solution()
print(s.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))