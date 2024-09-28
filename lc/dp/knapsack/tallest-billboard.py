class Solution:
    def dp(self, i, diff, rods, memo):
        if i == len(rods):
            if diff == 0:
                return 0
            return -sys.maxsize
        if (i, diff) in memo:
            return memo[(i, diff)]

        op1 = rods[i] + self.dp(i + 1, diff + rods[i], rods, memo)  # add rods[i] to taller -> height increased
        op2 = self.dp(i + 1, diff - rods[i], rods, memo)  # add rods[i] to shorter -> height not increase
        op3 = self.dp(i + 1, diff, rods, memo)  # no add
        memo[(i, diff)] = max(op1, op2, op3)
        return memo[(i, diff)]

    def tallestBillboard(self, rods: List[int]) -> int:
        memo = {}
        return self.dp(0, 0, rods, memo)

    # def tallestBillboard(self, rods: List[int]) -> int:
    #     # dp knapsack
    #     # complexity: time O(3^n)
    #     def dp(i, s1, s2):
    #         if i == len(rods):
    #             if s1 == s2: return s1
    #             return -sys.maxsize
    #         mx = 0
    #         mx = max(mx, dp(i + 1, s1, s2))
    #         mx = max(mx, dp(i + 1, s1 + rods[i], s2))
    #         mx = max(mx, dp(i + 1, s1, s2 + rods[i]))
    #         return mx

    #     return dp(0, 0, 0)
