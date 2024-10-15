class Solution:
    def minimumSteps(self, s: str) -> int:
        # 2 pointers
        # time O(n), space O(1)
        n = len(s)
        swap = 0
        l = 0
        for r in range(n):
            if s[r] == "0":
                swap += r - l
                l += 1
        return swap
