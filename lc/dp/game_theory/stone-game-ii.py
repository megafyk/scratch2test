class Solution:
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
