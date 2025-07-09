class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # dp bottom up knapsack 0/1
        # time O(nlogn + n*k), space O(n)
        events.sort()
        n = len(events)
        start = [e[0] for e in events]
        next_idx = [bisect.bisect_left(start, e[1] + 1) for e in events]
        dp = [0] * (n+1)
        for _ in range(k):
            new_dp = [0] * (n+1)
            for j in range(n-1, -1, -1):
                new_dp[j] = max(new_dp[j+1], events[j][2] + dp[next_idx[j]])
            dp = new_dp
        return dp[0] 

class Solution2:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)

        def next(idx):
            l, r = idx + 1, n
            while l < r:
                m = l + (r - l) // 2
                if events[m][0] > events[idx][1]:
                    r = m
                else:
                    l = m + 1
            return l
        
        @cache
        def get_max(idx, k):
            if idx == n or k == 0:
                return 0
            val = 0
            val = events[idx][2] + get_max(next(idx), k - 1) # get idx
            val = max(val, get_max(idx + 1, k))  # skip idx
            return val

        return get_max(0, k)