class Solution:
    def total(self, n, index, top):
        left = max(top-index, 0)
        total_left = ((top - left + 1) * (top + left)) // 2
        right = max(top-((n-1)-index), 0)
        total_right = ((top - right + 1) * (top + right)) // 2
        return total_left + total_right - top

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n
        l,r = 0, maxSum + 1
        while l < r:
            mid = l + (r - l) // 2
            if self.total(n, index, mid) > maxSum:
                r = mid
            else:
                l = mid + 1
        return l
