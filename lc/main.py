class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(t)
        n = len(s)
        prefix = [0] * n
        for i in range(m):
            nw_prefix = [0] * n
            for j in range(n):
                print(i,j, t[0], s[1])
                if t[i] == s[j]:
                    t = max(1, prefix[j])
                    nw_prefix[j] = t + (nw_prefix[j-1] if j > 0 else 0)
            prefix = nw_prefix
        return prefix[-1]