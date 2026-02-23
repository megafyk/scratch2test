class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = -1
        while n > 0:
            if prev == -1:
                prev = n & 1
            elif (n & 1) == prev:
                return False
            prev = n & 1
            n >>= 1
        return True