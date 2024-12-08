class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # heap
        # time O(nlogn), space O(n)
        events = sorted(events)
        pq = []
        mx = 0
        mx_val = 0
        for s,e,v in events:
            while pq and pq[0][0] < s:
                end, val = heappop(pq)
                mx_val = max(mx_val, val)
            mx = max(mx, v + mx_val)
            heappush(pq, (e, v))
        return mx
