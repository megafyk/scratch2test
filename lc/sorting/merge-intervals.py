class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorting + greedy
        # time O(nlogn), space O(n)
        intervals = sorted(intervals, key=lambda x: x[0])

        n = len(intervals)
        cur = intervals[0]
        res = []
        for i in range(1, n):
            s = intervals[i][0]
            e = intervals[i][1]
            if cur[1] >= s: # do merge
                cur[1] = e if cur[1] < e else cur[1]
            else:
                res.append(cur)
                cur = intervals[i]
        res.append(cur)
        return res

