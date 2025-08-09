class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0

class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        cnt = 0
        for i in range(32):
            cnt += (n >> i) & 1
            if cnt > 1:
                return False
        return cnt == 1
