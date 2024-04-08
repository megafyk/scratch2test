import heapq


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total_stones = 0
        for i in range(len(piles)):
            total_stones += piles[i]
            piles[i] = -piles[i]
        
        heapq.heapify(piles)
        
        taken_stones = 0
        
        for i in range(k):
            stones = heapq.heappop(piles)
            take = (-stones) // 2
            taken_stones += take
            remain = (-stones) - take
            heapq.heappush(piles, -remain)

        return total_stones - taken_stones