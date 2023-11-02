class Solution:
    def mySqrt(self, n: int) -> int:
        left, right = 0, n + 1
        while left < right:
            mid = left + (right - left) // 2
            if mid ** 2 > n:
                right = mid
            else:
                left = mid + 1
        return left - 1
