class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        # dp topdown unbounded knapsack
        # time O(n^2), space O(n^2)
        deno = []
        n = len(numWays)
        
        def count(target, idx, memo):
            if target == 0:
                return 1
            if target < 0:
                return 0
            if idx == len(deno):
                return 0

            if (target, idx) in memo: return memo[(target, idx)]
            way_idx = count(target - deno[idx], idx, memo)
            way_no_idx = count(target, idx + 1, memo)
            memo[(target, idx)] = way_idx + way_no_idx
            return memo[(target, idx)]

        if numWays[0] != 0:
            if numWays[0] > 1:
                return []
            else:
                deno.append(1)

        for i in range(n):
            memo = {}
            t = count(i + 1, 0, memo)
            if t != numWays[i]:
                if t == numWays[i] - 1:
                    deno.append(i + 1)
                else:
                    return []

        return sorted(deno)
