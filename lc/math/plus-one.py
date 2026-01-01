class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] = digits[i] + plus
            if digits[i] > 9:
                digits[i] = 0
                plus = 1
            else:
                plus = 0
        return digits if plus == 0 else [1] + digits