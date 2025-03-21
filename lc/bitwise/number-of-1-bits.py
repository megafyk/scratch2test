class Solution:
    def hammingWeight(self, n: int) -> int:
        # bitwise
        # time O(N), space O(1)
        res = 0
        for i in range(32):
            res += 1 if (n >> i & 1) else 0
        return res