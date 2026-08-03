class Solution:
    def stoneGameIII(self, nums: List[int]) -> str:
        n = len(nums)
        inf = 10**9+7
        dp = [-inf] * (n+1)
        dp[-1] = 0
        for i in range(n-1,-1,-1):
            if i <= n - 3:
                dp[i] = max(
                    nums[i] - dp[i+1],
                    nums[i] + nums[i+1] - dp[i+2],
                    nums[i] + nums[i+1] + nums[i+2] - dp[i+3]
                )
            elif i <= n - 2:
                dp[i] = max(
                    nums[i] - dp[i+1],
                    nums[i] + nums[i+1] - dp[i+2]
                )
            else:
                dp[i] = nums[i] - dp[i+1]

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"
