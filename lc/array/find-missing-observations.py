class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # complexity: time O(max(m,n)), mem O(n)
        m = len(rolls)
        s1 = sum(rolls)
        s2 = mean * (n + m) - s1
        if s2 < 0:
            return []
        base = s2 // n
        if base > 6 or base == 0:
            return []
        res = [base] * n
        remain = s2 % n
        i = 0
        while remain > 0:
            if i == n:
                i = 0
            res[i] += 1
            if res[i] > 6:
                return []
            i += 1
            remain -= 1
        return res
