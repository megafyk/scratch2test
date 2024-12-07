class Solution:
    def can_not_divide(self, candies, k, max_candies):
        for pile in candies:
            can = math.floor(pile / max_candies)
            k -= can
            if k <= 0: return False
        return k > 0

    def maximumCandies(self, candies: List[int], k: int) -> int:
        # binary search
        # time O(n + nlogn), space O(1)
        total = sum(candies)
        if total < k: return 0
        l, r = 1, math.ceil(total / k) + 1
        while l < r:
            mid = l + (r-l) // 2
            if self.can_not_divide(candies, k, mid):
                r = mid
            else:
                l = mid + 1
        return l-1
