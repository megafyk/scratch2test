class Solution:
    def countMonobit(self, n: int) -> int:
        i = 0
        cnt = 0
        while (1 << i) - 1 <= n:
            cnt += 1
            i += 1
        return cnt