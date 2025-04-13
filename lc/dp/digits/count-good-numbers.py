class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # exponential + recursion
        # time O(logN), space O(1)
        mod = 10 ** 9 + 7 
        def pow(x,y):
            res, mul = 1,x
            while y > 0:
                if y % 2 == 1:
                    res = res * mul % mod
                mul = mul * mul % mod
                y //= 2
            return res
        return (pow(5, (n+1) // 2) * pow(4, n // 2)) % mod