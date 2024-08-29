class Solution:
    def gcd(self, a,b):
        while a%b:
            a, b = b, a % b
        return b

    def calc(self, x, y):
        x1, x2 = x.split("/")
        y1, y2 = y.split("/")
        a = int(x1) * int(y2) + int(x2) * int(y1)
        b = int(x2) * int(y2)
        gcd = self.gcd(a, b)
        return f'{a//gcd}/{b//gcd}'


    def fractionAddition(self, expression: str) -> str:
        # simulation step with gcd
        # complexity: O(n), mem O(1)
        i = 0
        cur = "0/1"
        for j in range(1, len(expression)):
            if expression[j] == "+" or expression[j] == "-":
                new_cur = expression[i:j]
                cur = self.calc(cur, new_cur)
                i = j
            elif j == len(expression) - 1:
                new_cur = expression[i:j+1]
                cur = self.calc(cur, new_cur)
        return cur
