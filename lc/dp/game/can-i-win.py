from functools import cache


class Solution:
    def canIWin(self, n: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True

        # If even using all numbers can't reach desiredTotal, nobody can win
        if n * (n + 1) // 2 < desiredTotal:
            return False

        @cache
        def dp(mask, total) -> bool:
            if total >= desiredTotal: # prev player already won
                return False
            for i in range(n):
                b = (mask >> i) & 1
                if b == 0:
                    nw_mask = mask | (1 << i)
                    if not dp(nw_mask, total + (i + 1)):
                        return True
            return False

        return dp(0, 0)
