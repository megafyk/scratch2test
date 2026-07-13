class Solution:
    def reverse(self, x: int) -> int:
        pre = 1
        if x < 0:
            x = -x
            pre = -1

        x = -x if x < 0 else x
        reversed_x = 0
        bound = (1 << 31) - 1

        while x > 0:
            d = x % 10
            reversed_x = reversed_x * 10 + d
            if reversed_x >= bound:
                return 0
            x //=10

        return pre * reversed_x
