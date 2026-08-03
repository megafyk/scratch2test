class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True

class Solution1:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = list(piles)
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j-1])
        return dp[-1] > 0
