from collections import Counter
from functools import cmp_to_key


class Solution:
    def cmp(self, a, b):
        if a[1] == b[1]:
            return 1 if a[0] < b[0] else -1
        elif a[1] > b[1]:
            return 1
        else:
            return -1

    def frequencySort(self, nums: List[int]) -> List[int]:
        # complexity: time O(nlogn), mem O(n)
        cnt = Counter(nums)
        freq = sorted(cnt.items(), key=cmp_to_key(self.cmp))
        res = []
        for v, c in freq:
            res.extend([v] * c)
        return res
