class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        # dp digits
        # time O(log(n)*2*10), space O(log(n)*2*10)
        digits = list(map(int, str(n)))

        @cache
        def count(pos, tight, mask):
            if pos == len(digits): return 1 # found a non repeated num
            limit = digits[pos] if tight else 9
            res = 0
            for d in range(limit+1):
                if not mask & (1 << d):
                    new_tight = tight and d == limit
                    new_mask = mask if mask == 0 and d == 0 else mask | (1 << d)
                    res += count(pos + 1, new_tight, new_mask)
            return res
        total_non_repeated = count(0,True,0) - 1 # exclude 0
        return n - total_non_repeated
