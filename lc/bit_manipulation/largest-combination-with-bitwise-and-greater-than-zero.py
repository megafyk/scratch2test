class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # bitwise
        # time O(24 * n), space O(1)
        mx = 0
        for i in range(24):
            cnt = 0
            for num in candidates:
                if (num >> i & 1) == 1:
                    cnt += 1
            mx = max(mx, cnt)
        return mx
