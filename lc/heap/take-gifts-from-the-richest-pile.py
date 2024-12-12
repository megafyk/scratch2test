class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # max heap
        # time O(nlogn), space O(n)
        pq = []
        for g in gifts:
            heappush(pq, -g)

        while k > 0:
            k -= 1
            g = -heappop(pq)
            r = math.floor(math.sqrt(g))
            heappush(pq, -r)

        return -sum(pq)
