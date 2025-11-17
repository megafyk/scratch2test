from functools import cache
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0: return False
        target = total // k
        n = len(nums)
        @cache
        def dp(mask, cur, kk):
            if kk == k: return True
            if cur == target:
                return dp(mask, 0, kk+1)

            for i in range(n):
                if (mask >> i) & 1 == 0:
                    nw_mask = mask | (1 << i)
                    if dp(nw_mask, cur + nums[i], kk):
                        return True
            return False
        return dp(0,0,0)