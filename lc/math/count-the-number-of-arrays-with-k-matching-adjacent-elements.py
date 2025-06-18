class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        # math combinatorics
        # time O(1), space O(1)
        mod = 10 ** 9 + 7
        cnt_k_pairs_equal = comb(n-1, k)
        cnt_remain_diff = m*((m-1)**(n-1-k))
        return (cnt_k_pairs_equal * cnt_remain_diff) % mod