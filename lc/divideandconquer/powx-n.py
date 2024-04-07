class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1/self.myPow(x, -n)
        
        tmp = self.myPow(x, n // 2)
        tmp = tmp * tmp
        return tmp * x if n & 1 else tmp