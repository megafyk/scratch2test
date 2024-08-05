class Solution:
    def climbStairs(self, n: int) -> int:
        # dp route
        # complexity: time O(n), mem O(1)
        if n == 1:
            return 1
        dp1, dp2 = 1, 2
        for i in range(3, n + 1):
            dp2, dp1 = (dp1 + dp2), dp2
        return dp2
