class Solution:
    def dp(self, expression, memo):
        if expression in memo: return memo[expression]
        arr = []
        for idx, ch in enumerate(expression):
            if ch in "+-*":
                p1 = self.dp(expression[:idx], memo)
                p2 = self.dp(expression[idx+1:], memo)
                for a in p1:
                    for b in p2:
                        if ch == "+":
                            arr.append(a+b)
                        elif ch == "-":
                            arr.append(a-b)
                        else:
                            arr.append(a*b)
        memo[expression] = arr or [int(expression)]
        return memo[expression]

    def diffWaysToCompute(self, expression: str) -> List[int]:
        # dp compute all possibles
        # complexity: O(n*2^n), space O(n^2*2^n)
        memo = {}
        return self.dp(expression, memo)
