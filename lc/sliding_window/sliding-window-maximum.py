class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # sliding window, decresing monotonic queue
        # time O(N), space O(N)
        q = deque()
        res = []
        for i, num in enumerate(nums):
            while q and q[-1][0] < num:
                q.pop()
            q.append((num, i))
            if q[0][-1] <= i-k:
                q.popleft()
            if i + 1 >= k:
                res.append(q[0][0])
        return res
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     # sliding window + max heap
    #     # time O(NlogN), space O(N)
    #     pq = []
    #     res = []
    #     for i,num in enumerate(nums):
    #         heappush(pq, (-num, i))
    #         if i + 1 >= k:
    #             while pq[0][1] <= i-k:
    #                 heappop(pq)
    #             res.append(-pq[0][0])
    #     return res