import math


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def enough(mid):
            count = mid//a + mid//b + mid//c - mid//ab - mid//bc - mid//ca + mid//abc
            return count >= n
        ab = a*b // math.gcd(a, b)
        bc = b*c // math.gcd(b, c)
        ca = c*a // math.gcd(c, a)
        abc = ab * c // math.gcd(ab, c)
        left, right = 1, 2 * 10 ** 9
        while left < right:
            mid = left + (right - left) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1

        return left


s = Solution()
print(s.nthUglyNumber(3, 2, 3, 5))
