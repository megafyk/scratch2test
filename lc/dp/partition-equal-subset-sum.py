class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if s % 2: return False
        s //= 2
        
        dp = [[True] * (n+1) for _ in range(s+1)]
        
        for i in range(0, n+1):
            dp[0][i] = True
        
        for i in range(1, s+1):
            dp[i][0] = False
            
        for i in range(1, s+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i][j-1]
                if i >= nums[j-1]:
                    dp[i][j] = dp[i][j] or dp[i-nums[j-1]][j-1]

        return dp[s][n]