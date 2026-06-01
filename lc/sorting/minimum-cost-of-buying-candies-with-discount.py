class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # sorting
        # time O(nlogn), space O(1)
        cost.sort(reverse=True)
        n = len(cost)
        mi_cost = 0
        for i in range(0, n, 3):
            mi_cost += cost[i]
            if i + 1 < n:
                mi_cost += cost[i + 1]
        return mi_cost
