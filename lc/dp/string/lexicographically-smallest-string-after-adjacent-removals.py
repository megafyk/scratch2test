class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        # dp string
        # time O(n^3), space O(n^3)
        n = len(s)
        
        def conse(c1, c2):
            idx1 = ord(c1) - ord("a")
            idx2 = ord(c2) - ord("a")
            return abs(idx1 - idx2) == 1 or abs(idx1 - idx2) == 25

        @cache
        def empty(i, j):
            if i > j:
                return True
            if conse(s[i], s[j]) and empty(i + 1, j - 1):
                return True
            return any(empty(i, k) and empty(k + 1, j) for k in range(i + 1, j, 2))

        @cache
        def dp(i):
            if i == n:
                return ""
            ans = s[i] + dp(i + 1)
            for j in range(i + 1, n, 2):
                if empty(i, j):
                    ans = min(ans, dp(j + 1))
            return ans
        
        return dp(0)
