class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        start, end = [], []
        for item in intervals:
            start.append(item[0])
            end.append(item[1])
        start = sorted(start)
        end = sorted(end)
        s, e = 0, 0
        mx_groups = 0
        cur_group = 0

        while s < n:
            if start[s] <= end[e]:
                cur_group += 1
                s += 1
            else:
                cur_group -=1
                e += 1
            mx_groups = max(mx_groups, cur_group)

        return mx_groups