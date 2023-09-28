from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = [[] for _ in range(len(s))]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i, len(s)):
                if j - i <= 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

                if dp[i][j]:
                    ans[j-i].append(s[i:j + 1])

        ans = [arr for arr in ans if arr]
        print(dp)
        return ans

s = Solution()
print(s.partition('aab'))
