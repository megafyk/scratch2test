class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # time O(nlogn + n ^ (target / min(candidates))), space O(target / min(candidates))
        candidates.sort()
        n = len(candidates)
        res = []
        def dfs(start, target, comb):
            nonlocal res
            if target < 0:
                return

            if target == 0:
                res.append(comb)
                return

            for i in range(start, n):
                num = candidates[i]
                nw_comb = comb[::]
                nw_comb.append(num)
                dfs(i, target - num, nw_comb)

        dfs(0, target, [])
        return res
