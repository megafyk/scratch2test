class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        # dp knapsack 0/1
        # time O(n^2), space O(n)
        mod = 10**9 + 7
        nums = [i for i in range(1, math.ceil(n ** (1 / x)) + 1)]
        dp = [0] * (n + 1)
        dp[0] = 1

        for num in nums:
            power = num**x
            nw_dp = list(dp)
            for j in range(power, n + 1):
                nw_dp[j] = (nw_dp[j] + dp[j - power]) % mod
            dp = nw_dp
        return dp[n]


class Solution1:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9 + 7
        nums = [i for i in range(1, math.ceil(n ** (1 / x)) + 1)]

        @cache
        def dfs(idx, cur):
            if cur == 0:
                return 1
            if cur < 0:
                return 0
            if idx == len(nums):
                return 0
            return dfs(idx + 1, cur - nums[idx] ** x) + dfs(idx + 1, cur)

        return dfs(0, n) % mod
