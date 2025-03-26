class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # sorting + interval
        # time O(NlogN), space O(N)
        x = []
        y = []
        for x1,y1,x2,y2 in rectangles:
            x.append((x1,x2))
            y.append((y1,y2))
        x = sorted(x)
        y = sorted(y)
        def count_non_overlap(intervals):
            cnt = 0
            prev = -1
            for start,end in intervals:
                if start >= prev:
                    cnt += 1
                prev = max(prev, end)
            return cnt
        return max(count_non_overlap(x), count_non_overlap(y)) >= 3