from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = []
        n = len(s)

        for i in range(n + 1):
            dp.append([])  # create dp of size n+1

        dp[-1].append([])  # because for s[n:] i.e. empty string ,  answer = [[]]

        # dp[i] store all possible palindrome partitions of string s[i:]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                curr = s[i:j]  # cosider each substring of s start from i-th character

                if curr == curr[::-1]:  # if substring is palindrome

                    # Consider first element of each partition is curr then add curr in the front of all partitions of string s[j:]  , which are already stored in dp[j]
                    for e in dp[j]:
                        dp[i].append([curr] + e)

        return dp[0]  # All palindrome partitions of s[0:] = s


s = Solution()
print(s.partition('aab'))
