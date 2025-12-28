class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0: return -1
        cnt = 1
        r = 1
        acc = 1
        while True:
            r = (r * 10) % k
            acc += r
            cnt += 1
            if acc % k == 0:
                break
        return cnt