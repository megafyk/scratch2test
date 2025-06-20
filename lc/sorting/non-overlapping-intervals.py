class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sorting + greedy
        # time O(nlogn), space O(1)
        cnt = 1
        intervals = sorted(intervals, key=lambda x: x[1])
        end = intervals[0][1]
        n = len(intervals)
        for i in range(1, n):
            s = intervals[i][0]
            e = intervals[i][1]

            if s >= end:
                end = e
                cnt += 1

        return n - cnt