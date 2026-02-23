class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # string
        # time O(n), space O(1)
        cur = 1
        prev = 0
        cnt_sub = 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                cnt_sub += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1
        return cnt_sub + min(prev, cur)