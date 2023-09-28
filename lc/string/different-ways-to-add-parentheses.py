from typing import List


class Solution:
    def __init__(self):
        self.mem = {}
    def diffWaysToCompute(self, sub: str) -> List[int]:
        def is_int_number(sub) -> bool:
            try:
                int(sub)
                return True
            except ValueError:
                return False

        def cal(x, y, op) -> int:
            if op == "*":
                return x * y
            elif op == "+":
                return x + y
            else:
                return x - y
        if sub in self.mem:
            return self.mem[sub]

        if is_int_number(sub):
            self.mem[sub] = [int(sub)]
            return [int(sub)]
        res = []
        for i in range(len(sub)):
            if sub[i] in "+-*":
                l = self.diffWaysToCompute(sub[:i])
                r = self.diffWaysToCompute(sub[i + 1:])
                for x in l:
                    for y in r:
                        res.append(cal(x, y, sub[i]))
        self.mem[sub] = res
        return res


s = Solution()
print(s.diffWaysToCompute("2*3*4"))
