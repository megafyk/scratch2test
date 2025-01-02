class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # dp count distinct ways -> avoid tle
        # time O(high), space O(high)
        mod = 10 ** 9 + 7
        @cache
        def count(cur_len):
            if cur_len > high: return 0
            res = 1 if cur_len >= low and cur_len <= high else 0
            res += count(cur_len + zero) % mod
            res += count(cur_len + one) % mod
            return res % mod

        return count(0) % mod
