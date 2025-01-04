class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        # dp string
        # time O(n), space O(1)
        n = len(s)
        dp = [0] * 26
        curlen = 0
        for i in range(n):
            if i > 0 and ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25:
                curlen += 1
            else:
                curlen = 1
            idx = ord(s[i]) - ord('a')
            dp[idx] = max(dp[idx], curlen)
        return sum(dp)
