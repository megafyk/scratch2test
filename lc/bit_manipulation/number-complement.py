class Solution:
    def findComplement(self, num: int) -> int:
        bit_len = num.bit_length()
        mask = (1 << bit_len) - 1
        return num ^ mask

    # def findComplement(self, num: int) -> int:
    #     ans = 0
    #     tmp = 0
    #     for i in range(0, 32):
    #         bit = ((num >> i) & 1)
    #         if bit:
    #             tmp += 2 ** i
    #             if tmp == num:
    #                 break
    #         else:
    #             ans += 2 ** i
    #     return ans
