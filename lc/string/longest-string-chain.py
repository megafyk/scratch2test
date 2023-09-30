from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        ans = 1
        dp = {}
        for word in sorted(words, key=len):
            dp[word] = 1
            for i in range(len(word)):
                p_word = word[:i] + word[i + 1:]
                if p_word in dp:
                    dp[word] = max((dp[word]), dp[p_word] + 1)
                    ans = max(ans, dp[word])

        return ans


s = Solution()
print(s.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))
