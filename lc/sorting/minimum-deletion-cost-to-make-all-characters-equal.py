class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        cost_c = [0] * 26
        for i, c in enumerate(s):
            cost_c[ord(c) - ord('a')] += cost[i]
        cost_c.sort()
        return sum(cost_c) - cost_c[-1]