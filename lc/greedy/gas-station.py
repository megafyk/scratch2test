from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # nopath
        if sum(gas) - sum(cost) < 0:
            return -1
        # always can find a solution
        n = len(gas)
        tank = idx = 0
        for i in range(n):
            tank += gas[i] - cost[i]
            # there is no c between a -> b fullfill req
            if tank < 0:
                tank = 0
                idx = i + 1
        return idx
