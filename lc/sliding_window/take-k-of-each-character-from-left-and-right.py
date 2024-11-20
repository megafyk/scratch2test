class Solution:
    def pos(self, ch):
        return ord(ch) - ord("a")
    def takeCharacters(self, s: str, k: int) -> int:
        # sliding window
        # time O(n), space O(1)
        abc = [0,0,0]
        for ch in s:
            abc[self.pos(ch)] += 1
        if any(x < k for x in abc): return -1
        n = len(s)

        # aabaaaacaabc
        #    i  j   -> max
        mx = 0
        i = 0
        for j in range(n):
            abc[self.pos(s[j])] -= 1
            while min(abc) < k:
                abc[self.pos(s[i])] += 1
                i += 1
            mx = max(mx, j-i+1)
        return n - mx
