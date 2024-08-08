class Solution:
    def __init__(self):
        self.mod = 10**9 + 7

    def dp(self, n, step, x, y, memo):
        if step == n:
            return 1
        if (x, y, step) in memo:
            return memo[(x, y, step)]
        ans = 0

        steps = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        for dx, dy in steps:
            newx, newy = x + dx, y + dy
            if (
                (newx, newy) != (0, -1)
                and (newx, newy) != (0, 1)
                and 0 <= newx < 4
                and -1 <= newy <= 1
            ):
                ans += self.dp(n, step + 1, newx, newy, memo)
        memo[(x, y, step)] = ans
        return ans % self.mod

    def knightDialer(self, n: int) -> int:
        # dp distinct ways
        # complexity: time O(8^n), mem O(8^n)
        ans = 0
        cells = [
            (0, 0),
            (1, 0),
            (1, -1),
            (1, 1),
            (2, 0),
            (2, -1),
            (2, 1),
            (3, 0),
            (3, -1),
            (3, 1),
        ]
        memo = {}
        for x, y in cells:
            ans += self.dp(n, 1, x, y, memo)
        return ans % self.mod
