class Solution:
    def dp(self, nums, memo, i, j):
        if i > j:
            return 0
        if memo[i][j] != 0:
            return memo[i][j]
        mx = 0
        
        for k in range(i, j + 1):
            coins = nums[i - 1] * nums[k] * nums[j + 1] # k is the last burst balloon
            coins += self.dp(nums, memo, i, k - 1) + self.dp(nums, memo, k + 1, j)
            mx = max(mx, coins)
        memo[i][j] = mx
        return mx

    def maxCoins(self, nums: List[int]) -> int:
        # dp matrix chain multiplication
        # complexity: time O(n^3), mem O(n^2)
        n = len(nums)
        nums = [1] + nums + [1]
        memo = [[0] * (n+2) for _ in range(n+2)]
        return self.dp(nums, memo, 1, n)
