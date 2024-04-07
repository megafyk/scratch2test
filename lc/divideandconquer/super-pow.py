class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        for digit in b:
            res = (pow(res, 10) * pow(a, digit)) % 1337
        return res
    
    # def pow(self, base, exp):
    #     if exp == 0:
    #         return 1
    #     if exp == 1:
    #         return base
    #     res = self.pow(base, exp//2)
    #     res = res * res
    #     return res * base if exp & 1 else res