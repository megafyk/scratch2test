class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        for i in range(1,n//7+1):
            res += 7*(i+3)
        start = n // 7 + 1
        end = start + n%7 - 1
        res += (end+start)*(n%7) // 2
        return res

class Solution1:
    def totalMoney(self, n: int) -> int:
        res = 0
        start = 1
        cur = 1
        for i in range(1, n + 1):
            res += cur
            cur += 1
            if i % 7 == 0:
                start += 1
                cur = start
        return res