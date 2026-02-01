class Solution:
    def minimumMoves(self, s: str) -> int:
        # string
        # time O(n), space O(1)
        cnt = 0
        i = 0
        while i < len(s):
            if s[i] == "O":
                i += 1
            else:
                cnt += 1
                i += 3
        return cnt