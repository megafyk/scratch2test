class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # N = len(nums)
        # time O(N), space O(N)
        eq_idx = defaultdict(list)
        res = inf
        for idx, num in enumerate(nums):
            eq_idx[num].append(idx)
            if len(eq_idx[num]) >= 3:
                #dist = abs(eq_idx[num][-1] - eq_idx[num][-2]) + abs(eq_idx[num][-2] - eq_idx[num][-3]) + abs(eq_idx[num][-3] - eq_idx[num][-1])
                dist = 2 * (eq_idx[num][-1] - eq_idx[num][-3])
                res = min(res, dist)
        return res if res != inf else -1