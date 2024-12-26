class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp distinct ways bottom up
        # time O(n*target), space O(target)
        n = len(nums)

        dp = defaultdict(int)
        dp = {nums[0]: 1, -nums[0]: 1}
        if nums[0] == 0: dp[0] = 2
        for i in range(1, n):
            new_dp = defaultdict(int)
            for k,v in dp.items():
                new_dp[k + nums[i]] += dp[k]
                new_dp[k - nums[i]] += dp[k]
            dp = new_dp
        if target not in dp: return 0
        return dp[target]


# from collections import defaultdict

# class Solution:
#     def dp(self, nums, n, target, memo, i, s):
#         if i >= n:
#             return 1 if s == target else 0
#         if (i,s) in memo: return memo[(i,s)]
#         plus = self.dp(nums, n, target, memo, i+1, s + nums[i])
#         minus = self.dp(nums, n, target, memo, i+1, s - nums[i])
#         memo[(i,s)] = plus + minus
#         return memo[(i,s)]

#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         # knapsack topdown
#         # complexity: time O(n*target), mem O(n*target)
#         n = len(nums)
#         if sum(nums) < target:
#             return 0
#         memo = defaultdict(int)
#         return self.dp(nums, n, target, memo, 0, 0)
