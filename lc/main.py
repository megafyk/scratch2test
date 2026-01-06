from collections import defaultdict
from typing import List
import sys


class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = nums[i] + prefix[i-1]
        
        pos = defaultdict(int)

        j = -1
        res = sys.maxsize
        for i,num in enumerate(nums):
            if num in pos:
                j = max(j, pos[num])
            pos[num] = i
            while prefix[i] - prefix[j] >= k:
                res = min(res, i-j)
                j += 1
        return res if res != sys.maxsize else -1

s = Solution()
# arr = [63,47,9,23,47,29,47,23,36,47,9]
# k = 121
arr = [5,5,1]
k = 5
print(s.minLength(arr, k))