class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (3 ** 19) % n == 0

class Solution1:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1: return False
        cur = 1
        while cur <= n:
            if cur == n: return True
            cur *= 3
        return False