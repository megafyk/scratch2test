class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # sorting
        # time O(nlogn), space O(1)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        res = 0
        prev = [-1, -1]
        for s, e in intervals:
            if prev[0] <= s and e <= prev[1]:
                continue
            prev = [s, e]
            res += 1
        return res
