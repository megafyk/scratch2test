class Solution:
    def numSub(self, s: str) -> int:
        cnt = 0
        mod = 10**9 + 7
        res = 0
        for d in s:
            if d == "0":
                res += ((cnt * (cnt + 1)) // 2) % mod
                cnt = 0
            else:
                cnt += 1
        if cnt > 0:
            res += ((cnt * (cnt + 1)) // 2) % mod
        return res


class Solution1:
    def numSub(self, s: str) -> int:
        # 2 pointers
        # time O(n), space O(1)
        n = len(s)
        l = 0
        res = 0
        mod = 10**9 + 7
        for r in range(n):
            if s[r] == "0":
                size = r - l
                res += ((size * (size + 1)) // 2) % mod
                l = r + 1
        return res
