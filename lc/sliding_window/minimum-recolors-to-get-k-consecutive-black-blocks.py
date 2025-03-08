class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # sliding window
        # time O(N), space O(1)
        res = len(blocks) + 1
        n = len(blocks)
        i = 0
        cnt_w = 0
        for j in range(n):
            if blocks[j] == 'W':
                cnt_w += 1
            if j - i + 1 == k:
                res = min(res, cnt_w)
                if blocks[i] == 'W':
                    cnt_w -= 1
                i += 1
        return res