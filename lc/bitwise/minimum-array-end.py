class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # bitwise
        # time O(logn), space O(1)
        res = x
        i,j = 1,1
        while j <= n-1:
            if i & x == 0:
                if j & n-1:
                    res |= i
                j = j << 1
            i = i << 1
        return res
