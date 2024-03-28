from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        remain = 0
        for num in nums:
            if remain < 0:
                return False
            remain = max(remain, num)
            remain -= 1
        return True