class Solution:
    def findScore(self, nums: List[int]) -> int:
        # min heap
        # time O(nlogn), space O(n)
        mark = set()
        pq = []
        for idx, num in enumerate(nums):
            heappush(pq, (num, idx))
        score = 0
        while pq:
            num, idx = heappop(pq)
            if idx in mark: continue
            score += num
            mark.add(idx)
            mark.add(idx-1)
            mark.add(idx+1)
        return score
