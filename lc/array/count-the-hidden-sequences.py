class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # fix x as first number
        # prefix sum
        # time O(N), space O(1)
        mx = mi = 0
        cur = 0
        for diff in differences:
            cur += diff
            mx = max(mx, cur)
            mi = min(mi, cur)

        return max(0, (upper - lower + 1) - (mx-mi))