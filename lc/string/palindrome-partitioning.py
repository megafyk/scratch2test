from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        ans = []
        curr = []

        def dfs(i):

            if i >= len(s):
                ans.append(list(curr))

            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    curr.append(s[i:j + 1])
                    dfs(j + 1)
                    curr.pop()

        dfs(0)

        return ans


s = Solution()
# print(s.partition('aab')) #[["a","a","b"],["aa","b"]]
print(s.partition('abbab'))  # [["a","b","b","a","b"],["a","b","bab"],["a","bb","a","b"],["abba","b"]]
