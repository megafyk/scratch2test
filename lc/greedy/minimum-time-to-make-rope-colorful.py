from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        idx = 0
        n = len(colors)
        for i in range(n):
            s = 0
            max_c = 0
            while idx < n and colors[idx] == colors[i]:
                s += neededTime[idx]
                max_c = max(max_c, neededTime[idx])
                idx += 1
            res += s - max_c
            i = idx
        return res
