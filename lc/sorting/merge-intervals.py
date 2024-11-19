from functools import cmp_to_key
class Solution:
    def cmp(self, a, b):
        if a[0] == b[0]: return 1 if a[1] > b[1] else -1
        else: return 1 if a[0] > b[0] else -1

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # array sorting
        # time O(nlogn), space O(n)
        intervals = sorted(intervals, key=cmp_to_key(self.cmp))
        n = len(intervals)
        res = []
        cur = intervals[0]
        for i in range(1, n):
            if intervals[i][0] > cur[1]:
                res.append(cur)
                cur = intervals[i]
            else:
                cur[1] = intervals[i][1] if intervals[i][1] > cur[1] else cur[1]
        res.append(cur)
        return res
