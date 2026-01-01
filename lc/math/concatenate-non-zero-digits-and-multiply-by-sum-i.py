class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0: return 0
        s = str(n)
        sum_d = 0
        x = ''
        for d in s:
            sum_d += int(d)
            if d == "0": continue
            x += d
        return sum_d * int(x)