class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # dp string
        # time O(n*k*26*n), space O(n*k*26*n)

        # @cache
        def count(idx, k, prev, prev_cnt):
            if k < 0: return sys.maxsize
            if idx == len(s): return 0

            if s[idx] == prev:
                incr = 1 if prev_cnt in [1,9,99] else 0 # compress
                res = incr + count(idx+1, k, prev, prev_cnt+1)
            else:
                res = min(
                    count(idx+1,k-1,prev,prev_cnt), # remove s[i]
                    1 + count(idx+1,k, s[idx], 1) # keep s[i]
                )
            return res

        return count(0, k, "", 0)
