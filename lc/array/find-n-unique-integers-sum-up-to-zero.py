class Solution:
    def sumZero(self, n: int) -> List[int]:
        # array
        # time O(n), space O(n)
        cur = 1
        res = [0] if n % 2 else []
        n -= 1 if n % 2 else 0
        while n > 0:
            res.append(cur)
            res.append(-cur)
            cur += 1
            n-=2
        return res
