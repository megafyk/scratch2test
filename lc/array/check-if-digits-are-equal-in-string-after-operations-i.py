class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # brute force
        # time O(n^2), space O(n)
        s = [int(c) for c in s]
        while len(s) > 2:
            nw_s = []
            for i in range(len(s)-1):
                nw_s.append((s[i] + s[i+1]) % 10)
            s = nw_s
        return s[0] == s[-1]