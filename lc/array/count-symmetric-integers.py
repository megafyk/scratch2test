class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for num in range(low, high + 1):
            num_str = str(num)
            digits = len(num_str)
            if digits % 2: continue
            left = right = 0
            for i in range(digits//2):
                left += int(num_str[i])
                right += int(num_str[-i-1])
            if left == right: res += 1
        return res