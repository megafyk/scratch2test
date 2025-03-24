class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # arrays + sorting
        # time O(NlogN), space O(N)
        meetings = sorted(meetings)
        
        res = 0
        prev = 0
        
        for start, end in meetings:
            if start - prev >= 2:
                res += start - prev - 1
            prev = max(end, prev)

        res += days - prev
        return res