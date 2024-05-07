class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # complexity: time O(m*n), mem O(m)
        n = len(text1)
        m = len(text2)
        dp1 = [0] * (m + 1)

        for i in range(n):
            dp2 = [0] * (m + 1)
            for j in range(m):
                if text1[i] == text2[j]:
                    dp2[j + 1] = dp1[j] + 1
                else:
                    dp2[j + 1] = max(dp2[j], dp1[j], dp1[j + 1])
            dp1 = dp2
        return dp1[-1]