class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # bitwise
        # time O(N), space O(N)
        n = max(len(a), len(b))
        a = (n - len(a)) * "0" + a
        b = (n - len(b)) * "0" + b
        mem = 0
        res = []
        for i in range(n-1,-1 ,-1):
            t = int(a[i]) + int(b[i]) + mem
            if t == 2:
                mem = 1
                res.insert(0, "0")
            elif t > 2:
                mem = 1
                res.insert(0, "1")
            else:
                res.insert(0, str(t))
                mem = 0
        if mem == 1: res.insert(0,"1")
        return ''.join(res)