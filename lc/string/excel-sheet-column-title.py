class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # (2 * 26 ^ 2 + 17 * 26 + 6) = 26 * (2 * 26 ^ 1 + 17 * 26 ^ 0) + 6
        base = 26
        res = ""
        while columnNumber > 0:
            Z = (columnNumber - 1) % base
            ch = chr(Z + ord("A"))
            columnNumber = (columnNumber - 1) // base
            res = ch + res
        return res
