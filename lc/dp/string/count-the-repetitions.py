class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        # dp string
        # time O(len(s1) * len(s2) + n1), space O(len(s2))
        dp = {}
        for i in range(len(s2)):
            cnt = 0
            s1_i = i
            for ch in s1:
                if ch == s2[s1_i]:
                    s1_i += 1
                if s1_i == len(s2):
                    cnt += 1
                    s1_i = 0

            dp[i] = (cnt, s1_i)

        rep = 0
        idx = 0
        for _ in range(n1):
            cnt_rep, idx = dp[idx]
            rep += cnt_rep
        return rep // n2
