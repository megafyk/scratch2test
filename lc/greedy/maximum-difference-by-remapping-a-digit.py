class Solution:
    def minMaxDifference(self, num: int) -> int:
        # greedy
        # time O(logn), space O(1)
        num = str(num)
        mx = mi = ""
        mx_repl = ""
        mi_repl = num[0]
        for d in num:
            if d == mi_repl:
                mi += "0"
            else:
                mi += d

            if d == "9":
                mx += d
            else:
                if mx_repl == "":
                    mx_repl = d
                if d == mx_repl:
                    mx += "9"
                else:
                    mx += d

        return int(mx) - int(mi)
