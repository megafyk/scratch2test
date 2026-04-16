class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # array
        # n = len(nums), q = len(queries)
        # time O(n+q), space O(n)
        n = len(nums)
        nearest = [inf] * n
        found = {}
        for i in range(2*n):
            idx = (i+n) % n
            cur = nums[idx]
            if cur in found:
                j = found[cur]
                nearest[idx] = min(nearest[idx], i-j)
                nearest[j] = min(nearest[j], i-j)
            found[cur] = idx

        res = []
        for q in queries:
            if nearest[q] != n:
                res.append(nearest[q])
            else:
                res.append(-1)
        return res