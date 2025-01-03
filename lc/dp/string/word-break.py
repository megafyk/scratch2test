class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp string
        # time O(n^2), space O(n^2)
        wordDict = set(wordDict)
        n = len(s)
        # dp[i][j] -> s[i:j+1] is built by wordDict
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(i,n):
                if s[i:j+1] in wordDict:
                    dp[i][j] = True
                    dp[0][j] |= dp[0][i-1] if i > 0 else dp[i][j]
        return dp[0][n-1]
