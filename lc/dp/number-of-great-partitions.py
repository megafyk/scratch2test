class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        # dp knapsack => count # ways sum partition < k
        # time O(n*k), space O(k)
        mod = 10**9 + 7
        n = len(nums)
        if sum(nums) < 2 * k:
            return 0

        dp = [0] * k  # dp[s] = number of subsets with total exactly s
        dp[0] = 1
        for num in nums:
            for i in range(k - 1, -1, -1):
                if i >= num:
                    dp[i] = (dp[i] + dp[i - num]) % mod

        return (2**n - sum(dp) * 2) % mod


class Solution1:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        n = len(nums)
        if sum(nums) < 2 * k:
            return 0

        @cache
        def dfs(idx, cur):
            if cur >= k:
                return 0
            if idx >= n:
                return 1
            res = 0
            res += dfs(idx + 1, cur) % mod
            res += dfs(idx + 1, cur + nums[idx]) % mod
            return res % mod

        return (2**n - dfs(0, 0) * 2) % mod
