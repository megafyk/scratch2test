class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0
        i = 0
        for j in range(1, n):
            if prices[j] + 1 != prices[j-1]:
                t = (j-i)
                res += t*(t+1) // 2
                i = j
        t = n - i
        res += t*(t+1) // 2
        return res