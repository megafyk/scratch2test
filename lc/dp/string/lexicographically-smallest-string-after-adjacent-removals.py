class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        # dp string
        # time O(n^3), space O(n^3)
        n = len(s)
        
        def conse(c1, c2):
            idx1 = ord(c1) - ord("a")
            idx2 = ord(c2) - ord("a")
            return abs(idx1 - idx2) == 1 or abs(idx1 - idx2) == 25
        
        dp_empty = [[False] * n for _ in range(n)]
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                if conse(s[i], s[j]) and (l == 2 or dp_empty[i+1][j-1]):
                    dp_empty[i][j] = True
                    continue
                if l % 2 == 0:
                    for k in range(i+1,j,2):
                        if dp_empty[i][k] and dp_empty[k+1][j]:
                            dp_empty[i][j] = True
                            break

        dp = [""] * (n+1)
        for i in range(n-1, -1,-1):
            cur_ans = s[i] + dp[i+1]
            for j in range(i+1, n):
                if (j-i+1) % 2 == 0 and dp_empty[i][j]:
                    cur_ans = min(cur_ans, dp[j+1])
            dp[i] = cur_ans

        return dp[0]

        
        # @cache
        # def empty(i, j):
        #     if i > j:
        #         return True
        #     if conse(s[i], s[j]) and empty(i + 1, j - 1):
        #         return True
        #     return any(empty(i, k) and empty(k + 1, j) for k in range(i + 1, j, 2))

        # @cache
        # def dp(i):
        #     if i == n:
        #         return ""
        #     ans = s[i] + dp(i + 1)
        #     for j in range(i + 1, n):
        #         if empty(i, j):
        #             ans = min(ans, dp(j + 1))
        #     return ans

        # return dp(0)
        
        