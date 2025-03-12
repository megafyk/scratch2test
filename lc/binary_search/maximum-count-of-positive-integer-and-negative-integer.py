class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # binary search
        # time O(logN), space O(1)
        idx_neg = bisect.bisect_left(nums, 0)
        idx_pos = bisect.bisect_right(nums, 0)
        cnt_neg = idx_neg if idx_neg > 0 else 0
        cnt_pos = len(nums) - idx_pos if idx_pos < len(nums) else 0
        return max(cnt_neg, cnt_pos)