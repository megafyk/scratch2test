class Solution:
    def binaryGap(self, n: int) -> int:
        # string
        # time O(logn), space O(1)
        gap = 0
        s = bin(n)[2:]
        i = -1
        for j in range(len(s)):
            if s[j] == "1":
                if i != -1:
                    gap = max(gap, j-i)
                i = j
        return gap
