class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = 0
        full = numBottles
        empty = 0
        while full > 0:
            res += full
            empty += full
            full = 0
            if empty >= numExchange:
                empty -= numExchange
                full += 1
                numExchange += 1
        return res
            