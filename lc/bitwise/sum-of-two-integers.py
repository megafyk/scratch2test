class Solution:
    def getSum(self, a: int, b: int) -> int:
        # bitwise
        # time O(1), space O(1)
        mask = 0xFFFFFFFF
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        if a > 0x7FFFFFFF:  # Check if the result is negative
            a = ~(a ^ mask)
        return a