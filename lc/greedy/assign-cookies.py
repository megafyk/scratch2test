from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # complexity O(nlogn + mlogm), mem O(m+n)
        g = sorted(g)
        s = sorted(s)
        res = 0
        i = j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                res += 1
                i+=1
            j+=1
        return res
        