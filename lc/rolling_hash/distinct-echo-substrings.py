class Solution:

    def chr2int(self, chr):
        return ord(chr) - ord('a') + 1

    def sub_hash(self, i, j, hs, pw, mod):
        return (hs[j] - hs[i-1] * pw[j-i+1] % mod + mod) % mod

    def distinctEchoSubstrings(self, text: str) -> int:
        # complexity: time O(n), mem O(n)
        base = 27
        mod = 10 ** 9 + 7

        n = len(text)

        hs = [0] * (n+1)
        pw = [1] * (n+1)
        
        for i in range(1, n+1):
            hs[i] = (hs[i-1] * base + self.chr2int(text[i-1])) % mod
            pw[i] = (pw[i-1] * base) % mod
        res = set()
        for i in range(1, n+1):
            l = 1
            while i + 2*l - 1 < n+1:
                tmp = self.sub_hash(i, i+l-1, hs, pw, mod)
                if tmp == self.sub_hash(i+l, i+2*l-1, hs, pw, mod):
                    res.add(tmp)
                l += 1
        return len(res)