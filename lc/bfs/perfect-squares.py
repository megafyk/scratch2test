class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0

        for i in range(1, n+1):
            j = 1
            min_val = float('inf')
            while j*j <= i:
                min_val = min(min_val, 1 + dp[i-j*j])
                j+=1 
            dp[i] = min_val

        return dp[n] # type: ignore