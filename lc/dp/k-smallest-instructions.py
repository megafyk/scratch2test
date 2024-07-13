from math import comb

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        # dp + combinatorics
        # complexity: time O(v+h), mem O(v+h)
        v,h = destination

        remaining_v = v
        res = []
        for i in range(v + h):
            start_with_h = comb(v+h-i-1, remaining_v)
            if k <= start_with_h:
                res.append("H")
            else:
                res.append("V")
                remaining_v -= 1
                k -= start_with_h

        return ''.join(res)

