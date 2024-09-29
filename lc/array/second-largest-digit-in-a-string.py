class Solution:
    def secondHighest(self, s: str) -> int:
        # complexity: time O(n), space O(1)
        apprear = [None] * 9
        mx = mx_2 = -1
        for c in s:
            if c.isdigit():
                t = int(c)
                if t > mx:
                    mx_2 = mx
                    mx = t
                elif t < mx and t > mx_2:
                    mx_2 = t 
        return mx_2
