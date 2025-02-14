class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # min heap
        # time O(nlogn), space O(n)
        res = 0

        pq = []
        for num in nums:
            heappush(pq, num)
        
        while pq[0] < k:
            x = heappop(pq)
            y = heappop(pq)
            res += 1
            heappush(pq, x * 2 + y)

        return res