class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        mx, mi = -1, inf
        for n in nums:
            mx = max(mx, n)
            mi = min(mi, n)
        return k * (mx - mi)
