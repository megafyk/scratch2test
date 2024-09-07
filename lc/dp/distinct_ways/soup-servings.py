class Solution:
    def dp(self, memo, A, B):
        if A <= 0 and B <= 0: return 0.5
        if A <= 0: return 1
        if B <= 0: return 0
        if (A, B) in memo: return memo[(A, B)]
        ans = 0.25 * (
            self.dp(memo, A - 4, B - 0) +
            self.dp(memo, A - 3, B - 1) + 
            self.dp(memo, A - 2, B - 2) +
            self.dp(memo, A - 1, B - 3)
        )
        memo[(A, B)] = ans
        return ans

    def soupServings(self, n: int) -> float:
        memo = {}
        n = ceil(n/25)
        for i in range(1, n+1):
            if self.dp(memo, i, i) > 1 - 10 ** -5:
                return 1
        return self.dp(memo, n, n)
