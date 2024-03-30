from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        prev_idx = {}

        for i, num in enumerate(nums):
            if num in prev_idx and i - prev_idx[num] <= k:
                return True
            prev_idx[num] = i
        return False
