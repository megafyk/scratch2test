class Solution:
    def punishmentNumber(self, n: int) -> int:
        # backtrack
        # time O(n*2^log(n)), space O(log(n))

        def backtrack(i, digits):
            if i == 0 and not digits: return True
            if i < 0: return False
            is_punish = False
            for j in range(1, len(digits)+1):
                p1 = digits[:j]
                p2 = digits[j:]
                if backtrack(i-int(p1), p2):
                    return True
            return False

        res = 0
        for i in range(1, n+1):
            sqr = i * i
            if backtrack(i, str(sqr)):
                res += sqr
        return res
