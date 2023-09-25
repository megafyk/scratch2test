class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            dp = [0] * 26
            max_f, min_f = 0, 0
            for j in range(i, len(s)):
                char_idx = ord(s[j]) - ord('a')
                dp[char_idx] += 1
                max_f = max(max_f, dp[char_idx])
                if min_f >= dp[char_idx] - 1:
                    min_f = dp[char_idx]
                    for k in range(26):
                        if dp[k] > 0:
                            min_f = min(min_f, dp[k])
                ans += (max_f - min_f)
        return ans


s = Solution()
print(s.beautySum("aabcb"))
