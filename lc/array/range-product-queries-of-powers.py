class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # array
        # time O(q), space O(1)
        mod = 10 ** 9 + 7
        powers = []
        for i in range(32):
            if (n >> i) & 1 == 1:
                powers.append(2**i)
        prefix = [0] * len(powers)
        prefix[0] = powers[0]
        for i in range(1, len(powers)):
            prefix[i] = (prefix[i-1] * powers[i])

        res = []
        for s,e in queries:
            t = prefix[e]
            t //= prefix[s-1] if s > 0 else 1
            res.append(t % mod)
        return res