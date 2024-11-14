class Solution:
    def distribute(self, n, quantities, target):
        for q in quantities:
            n -= math.ceil(q/target)
        return n >= 0

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l,r = 1, max(quantities)
        while l < r:
            mid = l + (r - l) // 2
            if self.distribute(n, quantities, mid):
                r = mid
            else:
                l = mid + 1
        return l
