class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * n
        suffix[-1] = piles[-1]
        for i in range(n-2, -1 , -1):
            suffix[i] = piles[i] + suffix[i+1]
        

        dp = [[0] * (n + 1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for M in range(1, n+1):
                if i + 2 * M >= n:
                    dp[i][M] = suffix[i] # get all
                else:
                    for x in range(1, 2 * M + 1):
                        # gain = total - best_opponents
                        dp[i][M] = max(dp[i][M], suffix[i] - dp[i+x][max(M,x)])

        return dp[0][1] # alice go first with M = 1

class Solution1:
    def dfs(self, piles, alice, i, m, memo):
        if i == len(piles):
            return 0
        if (alice, i, m) in memo:
            return memo[(alice, i, m)]
        res = 0 if alice else sys.maxsize
        total = 0
        for x in range(1, 2 * m + 1):
            if i + x > len(piles):
                break
            total += piles[i + x - 1]
            if alice:
                res = max(res, total + self.dfs(piles, False, i + x, max(m, x), memo))
            else:
                res = min(res, self.dfs(piles, True, i + x, max(m, x), memo))
        memo[(alice, i, m)] = res
        return res

    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        return self.dfs(piles, True, 0, 1, memo)
