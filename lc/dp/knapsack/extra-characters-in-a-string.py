class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.word = False
class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for w in words:
            cur = self.root
            for c in w:
                idx = ord(c) - ord('a')
                if not cur.child[idx]:
                    cur.child[idx] = TrieNode()
                cur = cur.child[idx]
            cur.word = True
            

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # complexity: time O(n^2+m*k), space: O(n+m*k)
        n = len(s)
        root = Trie(dictionary).root

        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]
            cur = root
            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                if not cur.child[idx]:
                    break
                cur = cur.child[idx]
                if cur.word:
                    dp[i] = min(dp[i], dp[j+1])
        return dp[0]


    # def minExtraChar(self, s: str, dictionary: List[str]) -> int:
    # complexity: time O(n^3), space: O(n)
    #     n = len(s)
    #     dictionary = set(dictionary)

    #     dp = [0] * (n + 1)
    #     for i in range(n - 1, -1, -1):
    #         dp[i] = 1 + dp[i + 1]
    #         for j in range(i, n):
    #             if s[i : j + 1] in dictionary:
    #                 dp[i] = min(dp[i], dp[j + 1])
    #     return dp[0]

    # def dp(self, s, dictionary, i, memo):
    #     if i == len(s):
    #         return 0
    #     if i in memo:
    #         return memo[i]
    #     res = 1 + self.dp(s, dictionary, i + 1, memo)
    #     for j in range(i, len(s)):
    #         if s[i : j + 1] in dictionary:
    #             res = min(res, self.dp(s, dictionary, j + 1, memo))
    #     memo[i] = res
    #     return res

    # def minExtraChar(self, s: str, dictionary: List[str]) -> int:
    #     memo = {}
    #     return self.dp(s, dictionary, 0, memo)
