from typing import List


class Solution:
    def __init__(self):
        self.alphabet = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        ans = []

        d_2_chars = self.alphabet[digits[0]]

        if len(digits) == 1:
            return list(d_2_chars)

        for char in d_2_chars:
            for ele in self.letterCombinations(digits[1:]):
                ans.append(char + ele)
        return ans


s = Solution()
print(s.letterCombinations("23"))
print(s.letterCombinations(""))
print(s.letterCombinations("9"))
