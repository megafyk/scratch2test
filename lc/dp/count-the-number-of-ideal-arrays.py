class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        # dp combinatoric
        # time O(NlogM), space O(M)
        mod = 10 ** 9 + 7
        freq = {i:1 for i in range(1, maxValue)}
        res = maxValue # [1,1...1], [2,2...2]...,[maxValue,maxValue...maxValue] are valid
        for k in range(1, n): # k distinct value set non-decrease
            tmp = defaultdict(int)
            for x in freq:
                for m in range(2, maxValue//x + 1):
                    res += math.comb(n-1, k) * freq[x]
                    tmp[m*x] += freq[x]
            freq = tmp
            res %= mod
        return res