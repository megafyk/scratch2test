class Solution:
    def rotatedDigits(self, n: int) -> int:
        cnt_good = 0
        can_not_rotate = "347"
        can_rotate = "0125689"
        good_rotate = "2569"
        for t in range(1, n + 1):
            num = str(t)
            good = False
            for d in num:
                if d in can_not_rotate:
                    good = False
                    break
                if d in good_rotate:
                    good = True
            if good:
                cnt_good += 1
        return cnt_good
