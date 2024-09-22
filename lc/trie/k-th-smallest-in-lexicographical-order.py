class Solution:
    def count(self, n, cur):
        res = 0
        nei = cur + 1
        while cur <= n:
            res += min(nei, n + 1) - cur # n is inclusive -> n+1
            cur *= 10
            nei *= 10
        return res

    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        cur_idx = 1

        while cur_idx < k:
            steps = self.count(n, cur)

            if cur_idx + steps <= k:  # move to neighbor
                cur += 1
                cur_idx += steps
            else:
                cur *= 10
                cur_idx += 1
        return cur
