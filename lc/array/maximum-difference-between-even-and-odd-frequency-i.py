class Solution:
    def maxDifference(self, s: str) -> int:
        # array
        # time O(n), space O(1)
        freq = Counter(s)
        mx_odd = 0
        mi_even = sys.maxsize
        for v in freq.values():
            if v % 2 == 1:
                mx_odd = max(mx_odd, v)
            elif v % 2 == 0:
                mi_even = min(mi_even, v)
        return mx_odd - mi_even
