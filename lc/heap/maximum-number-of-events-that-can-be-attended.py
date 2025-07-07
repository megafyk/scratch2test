class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # min heap + sorting
        # time O(nlogn + n), space O(n)
        events = sorted(events)
        n = len(events)
        i = 0
        cur_day = 0
        pq = []
        res = 0
        while i < n or pq:
            if not pq:
                cur_day = events[i][0]
            
            while i < n and events[i][0] == cur_day:
                heappush(pq, events[i][1])
                i += 1
            
            while pq and pq[0] < cur_day: # remove events already ended
                heappop(pq)

            if pq:
                heappop(pq) # join event end ealiest
                res += 1
                cur_day += 1
        return res