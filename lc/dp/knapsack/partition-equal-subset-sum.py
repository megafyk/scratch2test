class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # dp knapsack 0/1
        # time O(N*S), space O(N*S)
        n = len(nums)
        s = sum(nums)
        if s % 2 != 0: return False
        dp = [[True] * (n+1) for _ in range(s//2 + 1)]

        for target in range(1, s//2 + 1):
            dp[target][0] = False

        for target in range(1, s//2 + 1):
            for j in range(1, n+1):
                dp[target][j] = dp[target][j-1] # no pick nums[j-1]
                if target >= nums[j-1]:
                    dp[target][j] = dp[target-nums[j-1]][j-1] or dp[target][j]
        return dp[-1][-1]