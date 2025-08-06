class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        cnt = 0
        for i in range(n):
            cnt += 1
            for j in range(n):
                if fruits[i] <= baskets[j]:
                    cnt -= 1
                    baskets[j] = 0
                    break
        return cnt