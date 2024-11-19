class Solution:
    def isHappy(self, n: int) -> bool:
        # time O(n), space O(n)
        cur = str(n)
        s = set()
        while True:
            total = 0
            for c in cur:
                total += int(c) ** 2
            if total in s:
                return False if total != 1 else True
            s.add(total)
            cur = str(total)
