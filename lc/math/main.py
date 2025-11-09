class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # math gcd
        # time O(log(max(num1, num2))), space O(1)
        res = 0
        while num1 != 0 and num2 != 0:
            if num1 > num2:
                res += num1 // num2
                num1, num2 = num2, num1 % num2
            else:
                res += num2 // num1
                num2, num1 = num1, num2 % num1
        return res