class Solution:
    def minChanges(self, s: str) -> int:
        # string greedy
        # time O(n), space O(1)
        change = 0
        for i in range(0,len(s)-1, 2):
            if (s[i] == "0" and s[i+1] == "1") or (s[i] == "1" and s[i+1] == "0"):
                change += 1
        return change
