from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def feasible(total):
            t = 1
            curr_sum = 0
            for n in nums:
                curr_sum += n
                if curr_sum > total:
                    curr_sum = n
                    t += 1
                    if t > k:
                        return False
            return True
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left
        
s = Solution()
print(s.splitArray([7,2,5,10,8], 2))