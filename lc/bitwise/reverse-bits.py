class Solution:
    def reverseBits(self, n: int) -> int:
        # bitwise
        # time O(N), space O(1)
        res = 0
        for i in range(32):
            if (n >> i) & 1 == 1:
                res += 1 << (31 - i)
        return res