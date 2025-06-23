class Solution:
    def fib(self, n: int) -> int:
        # dp + math
        # time O(n), space O(1)
        f0, f1 = 0,1
        for _ in range(n):
            f0,f1 = f1, f0 + f1
        return f0