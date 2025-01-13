class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        res = 0
        n = len(s)

        def count(l, r):
            cnt = 0
            while l < r:
                if s[l] != s[r]:
                    cnt += 1
                l += 1
                r -= 1
            return cnt

        @cache
        def dp(i, k):
            if n - i == k: return 0
            if k == 1: return count(i, n-1)
            res = sys.maxsize
            for j in range(i, n-k+1):
                res = min(res, count(i,j) + dp(j+1, k-1))
            return res

        res = dp(0, k)
        return res
