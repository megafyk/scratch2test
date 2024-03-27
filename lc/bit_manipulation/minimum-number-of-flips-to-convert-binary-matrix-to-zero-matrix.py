from typing import List


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        res = n*m + 1
        binstr = ''
        for i in range(n):
            for j in range(m):
                binstr += str(mat[i][j])

        s = int(binstr, 2)

        for mask in range(1<<n*m):
            d = self.flip(s, mask, n, m)
            if d != -1:
                res = min(res, d)


        return res if res != (n*m+1) else -1
    def flip(self, s, mask, n, m):
        for i in range(n*m):
            if self.test(mask, i):
                s = self.toggle(s, i)
                s = self.toggle(s, i+m) if i+m < m*n else s
                s = self.toggle(s, i-m) if i >= m else s
                s = self.toggle(s, i+1) if i%m < m-1 else s
                s = self.toggle(s, i-1) if i%m > 0 else s
        # all cell must be flip once -> total step = number of 1 bits in mask
        return mask.bit_count() if s == 0 else -1

    def test(self, mask, i):
        return (mask >> i) & 1 == 1
    
    def toggle(self, s, i):
        return s ^ (1 << i)
                