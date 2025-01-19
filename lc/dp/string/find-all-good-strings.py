class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        # dp string + kmp
        # time O(n*m^2), space O(n*m)
        m = len(evil)
        mod = 10**9 + 7
        pi = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and evil[i] != evil[j]:
                j = pi[j - 1]
            if evil[i] == evil[j]:
                j += 1
                pi[i] = j

        @cache
        def dp(idx, is_pre_s1, is_pre_s2, match_evil_len):
            if match_evil_len == m:
                return 0
            if idx == n:
                return 1

            start = ord(s1[idx]) if is_pre_s1 else ord("a")
            end = ord(s2[idx]) if is_pre_s2 else ord("z")
            res = 0
            for i in range(start, end + 1):
                cur_c = chr(i)
                tmp_evil_len = match_evil_len
                while tmp_evil_len > 0 and cur_c != evil[tmp_evil_len]:
                    tmp_evil_len = pi[tmp_evil_len - 1]
                if cur_c == evil[tmp_evil_len]:
                    tmp_evil_len += 1
                res += dp(
                    idx + 1,
                    is_pre_s1 and i == start,
                    is_pre_s2 and i == end,
                    tmp_evil_len,
                )

            return res

        return dp(0, True, True, 0) % mod
