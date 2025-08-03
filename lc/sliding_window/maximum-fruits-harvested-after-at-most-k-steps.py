class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # sliding window
        # time O(n), space O(1)
        n = len(fruits)

        l = r = 0
        cur_total = 0
        res = 0

        def cnt_step(l, r): # always start at startPos, get fruits in window l-r
            if fruits[l][0] >= startPos:
                return fruits[r][0] - startPos
            elif fruits[r][0] <= startPos:
                return startPos - fruits[l][0]
            else:
                return min(startPos - fruits[l][0], fruits[r][0] - startPos) + (
                    fruits[r][0] - fruits[l][0]
                )

        while r < n:
            cur_total += fruits[r][1]
            while l <= r and cnt_step(l, r) > k:
                cur_total -= fruits[l][1]
                l += 1
            res = max(res, cur_total)
            r += 1

        return res