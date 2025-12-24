class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        pq = []
        n = len(nums)
        res = 0
        for i in range(n):
            heappush(pq, -nums[i])
            if s[i] == "1":
                num = -heappop(pq)
                res += num
        return res 
                