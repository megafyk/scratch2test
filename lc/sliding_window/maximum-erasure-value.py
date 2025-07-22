class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # sliding window
        # time O(n), space O(n)
        n = len(nums)
        last_idx = defaultdict(int)
        last_idx[nums[0]] = 0
        prefix = [0] * n
        prefix[0] = nums[0]
        l = 0
        res = nums[0]
        for r in range(1, n):
            prefix[r] = prefix[max(0, r-1)] + nums[r]
            if nums[r] in last_idx:
                l = max(l, last_idx[nums[r]] + 1)
            last_idx[nums[r]] = r
            res = max(res, prefix[r] - (prefix[l-1] if l > 0 else 0))
        return res