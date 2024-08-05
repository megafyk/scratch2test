class Solution:
    def dp(self, n, k, target, memo):
        mod = 10**9 + 7
        if n == 0 and target == 0:
            return 1
        if n == 0 or target == 0:
            return 0
        if (n, target) in memo:
            return memo[(n, target)]
        ans = 0
        for i in range(1, k + 1):
            ans += self.dp(n - 1, k, target - i, memo) % mod
        ans %= mod
        memo[(n, target)] = ans
        return ans

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # dp with memo
        # complexity: time O(n*k*target), mem O(n*target)
        memo = {}
        return self.dp(n, k, target, memo)
