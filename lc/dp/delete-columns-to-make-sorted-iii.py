class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # dp lis string
        # time O(m*n*k), space O(n)
        m = len(strs)
        n = len(strs[0])
        dp = [1] * n

        def check(i, j):
            for word in strs:
                if ord(word[i]) < ord(word[j]):
                    return False
            return True

        for i in range(1, n):
            for j in range(i):
                if check(i,j):
                    dp[i] = max(dp[i], dp[j] + 1)

        return n - max(dp)
