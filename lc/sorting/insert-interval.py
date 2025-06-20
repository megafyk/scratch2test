class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # sorting + greedy
        # time O(nlogn), space O(n)
        bisect.insort(intervals, newInterval)
        cur = intervals[0]
        n = len(intervals)
        res = []
        for i in range(1, n):
            s = intervals[i][0]
            e = intervals[i][1]
            if cur[1] >= s:
                cur[1] = max(cur[1], e)
            else: 
                res.append(cur)
                cur = intervals[i]
        
        res.append(cur)
        return res
