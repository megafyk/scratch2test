class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        left = 0
        right = 0
        d_sub = {}
        ans = 0
        while right < len(s):
            if s[right] in d_sub:
                ans = max(ans, right - left)
                left = max(left, d_sub[s[right]])
            d_sub[s[right]] = right + 1
            right += 1
        return max(ans, right - left)


s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("tmmzuxt"))
