class Solution:
    def maxDiff(self, num: int) -> int:
        # greedy
        # time O(logn), space O(1)
        num = str(num)
        mx, mi = num, num
        for d in num:
            if d != "9":
                mx = mx.replace(d, "9")
                break
        for i, d in enumerate(num):
            if i == 0:
                if d != "1":
                    mi = mi.replace(d, "1")
                    break
            else:
                if d != "0" and d != num[0]:
                    mi = mi.replace(d, "0")
                    break
        return int(mx) - int(mi)
