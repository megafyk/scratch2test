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

class Solution1:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort(key=lambda x: x[0])
        suffix_mx = [0] * n
        suffix_mx[-1] = events[-1][2]
        for i in range(n-2,-1,-1):
            suffix_mx[i] = max(events[i][2], suffix_mx[i+1])
        res = 0

        for i in range(n):
            l,r = i+1, n-1
            idx = i
            while l <= r:
                mid = l + (r-l) // 2

                if events[i][1] < events[mid][0]:
                    idx = mid
                    r = mid - 1
                else:
                    l = mid + 1
            if idx < n and events[i][1] < events[idx][0]:
                res = max(res, events[i][2] + suffix_mx[idx])
            res = max(res, events[i][2])
        return res

class Solution2:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort(key=lambda x: x[0])
        res = 0
        pq = []
        mx = 0
        for i in range(n):
            while pq and pq[0][0] < events[i][0]:
                _, val = heappop(pq)
                mx = max(mx, val)
            res = max(res, mx + events[i][2])
            heappush(pq, (events[i][1], events[i][2]))
        return res
