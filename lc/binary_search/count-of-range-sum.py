class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # prefix sum + sorted list
        # time O(nlogn), space O(n)
        n = len(nums)
        sl = SortedList([0])
        prefix = 0
        res = 0
        for i in range(n):
            prefix += nums[i]
            l = bisect.bisect_left(sl, prefix - upper)
            r = bisect.bisect_right(sl, prefix - lower)
            res += (r-l)
            sl.add(prefix)
        return res
