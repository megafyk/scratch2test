class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # prefix sum
        # time O(q), space O(1)
        mod = 10**9 + 7
        prefix = []
        for i in range(32):
            if (n >> i) & 1 == 1:
                if len(prefix) == 0:
                    prefix.append(2**i)
                else:
                    prefix.append(prefix[-1] * 2**i)

        res = []
        for s, e in queries:
            t = prefix[e]
            t //= prefix[s - 1] if s > 0 else 1
            res.append(t % mod)
        return res