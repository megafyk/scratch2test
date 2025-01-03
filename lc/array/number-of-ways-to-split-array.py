class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # array prefix sum
        # time O(n), space O(n)
        n = len(nums)
        prefix_sum = [0] * n
        for i in range(n):
            prefix_sum[i] = nums[i] + (prefix_sum[i-1] if i > 0 else 0)

        res = 0
        for i in range(n-1):
            res += 1 if prefix_sum[i] >= prefix_sum[-1] - prefix_sum[i] else 0
        return res
