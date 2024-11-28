
from typing import List


class Solution:
    def __init__(self):
        self.dmap = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        d2chars = self.dmap[digits[0]]
        if len(digits) == 1:
            return list(self.dmap[digits[0]])
            
        for c in d2chars:
            for ele in self.letterCombinations(digits[1:]):
                res.append(c+ele)
        return res