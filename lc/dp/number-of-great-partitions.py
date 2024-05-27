class Solution:
    def helper(self, nums, n, k, dp, i, s1):
        if s1 >= k:
            return 0
        if i >= n:
            return 1
        if dp[i][s1]:
            return dp[i][s1]

        total = 0
        total += self.helper(nums, n, k, dp, i + 1, s1 + nums[i])
        total += self.helper(nums, n, k, dp, i + 1, s1)
        dp[i][s1] = total % self.mod
        return total

    def countPartitions(self, nums: List[int], k: int) -> int:
        # reduce number of dp state
        # complexity: time O(n*k), mem O(n*k)
        n = len(nums)
        s = sum(nums)
        # case s1 < k, s2 < k
        if s < 2 * k:
            return 0
        dp = [[None] * k for _ in range(n)]
        self.mod = 1000000007
        total_ways = 1 << n
        # case (s1 < k, s2 >= k) == (s1 >= k, s2 < k)
        invalid_ways = 2 * self.helper(nums, n, k, dp, 0, 0)
        return (total_ways - invalid_ways) % self.mod
