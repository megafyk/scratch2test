class Solution:
    def tribonacci(self, n: int) -> int:
        # dp
        # time O(n), space O(1)
        f0,f1,f2 = 0,1,1
        if n == 0: return f0
        if n == 1: return f1
        for i in range(3, n+1):
            f0,f1,f2 = f1,f2,f0+f1+f2
        return f2