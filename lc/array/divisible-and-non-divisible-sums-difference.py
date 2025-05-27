class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # array
        # time O(n), space O(1)
        num1 = num2 = 0
        for num in range(1,n+1):
            if num % m != 0:
                num1 += num
            else:
                num2 += num
        return num1 - num2