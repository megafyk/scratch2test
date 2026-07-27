class Solution:
    def maxProduct(self, n: int) -> int:
        # math
        # O(logn), space O(1)
        mx1, mx2 = 0,0
        while n > 0:
            d = n % 10
            if d >= mx2 >= mx1:
                mx1 = mx2
                mx2 = d
            elif mx2 > d >= mx1:
                mx1 = d
            n //= 10
        return mx1 * mx2
