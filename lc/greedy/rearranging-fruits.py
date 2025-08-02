class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # greedy
        # time O(n), space O(n)
        cnt = Counter(basket1)
        for b in basket2:
            cnt[b] -= 1
        last = []  # cost
        for k, v in cnt.items():
            if v % 2:
                return -1
            last += [k] * abs(v // 2)
        minx = min(basket1 + basket2) # indirect swap a <> x <> b = cost 2x 
        last.sort()
        return sum(min(2*minx, x) for x in last[0: len(last) // 2]) # first half cost, compare direct vs indirect swap
