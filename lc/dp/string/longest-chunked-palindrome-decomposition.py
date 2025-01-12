class Solution:
    def longestDecomposition(self, text: str) -> int:
        # dp + greedy
        # time O(n^2), space O(n)
        def dp(text):
            n = len(text)
            if n == 0: return 0
            if n == 1: return 1
            i = 1

            while i <= n - i:
                s1 = text[:i]
                s2 = text[n-i:]
                if s1 == s2:
                    return 2 + dp(text[i:n-i])
                i += 1
            return 1
        return dp(text)
