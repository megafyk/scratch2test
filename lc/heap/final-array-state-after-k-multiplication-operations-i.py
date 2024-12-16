class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = []
        for idx, num in enumerate(nums):
            heappush(pq, (num, idx))
        while k > 0:
            k-=1
            num, idx = heappop(pq)
            nums[idx] = num * multiplier
            heappush(pq, (num * multiplier, idx))
        return nums
