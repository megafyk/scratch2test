class Solution:
    def guessNumber(self, n: int) -> int:
        l,r = 1, n
        while l <= r:
            mid = l + (r-l) // 2
            if guess(mid) == 0: return mid
            elif guess(mid) == 1: l = mid + 1
            else: r = mid - 1
        return -1