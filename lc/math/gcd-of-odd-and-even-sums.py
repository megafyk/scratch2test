class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # math
        def gcd(a,b):
            if a > b:
                a,b = b,a
            while b > 0:
                a,b = b, a%b
            return a
        s = n * (n * 2 +1)
        s_odd = n * n
        s_even = s - s_odd
        return gcd(s_odd, s_even)
