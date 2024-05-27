from collections import defaultdict

class Solution:
    def dp(self, nums, n, target, memo, i, s):
        if i >= n:
            return 1 if s == target else 0
        if (i,s) in memo: return memo[(i,s)]
        plus = self.dp(nums, n, target, memo, i+1, s + nums[i])
        minus = self.dp(nums, n, target, memo, i+1, s - nums[i])
        memo[(i,s)] = plus + minus
        return memo[(i,s)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # knapsack topdown
        # complexity: time O(n*target), mem O(n*target)
        n = len(nums)
        if sum(nums) < target:
            return 0
        memo = defaultdict(int)
        return self.dp(nums, n, target, memo, 0, 0)