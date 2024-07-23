class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp 1bit is equal * 2
        # complexity: time O(n), mem O(n)
        res = [0] * (n + 1)

        for i in range(1, n + 1):
            res[i] = res[i // 2] + (i & 1)
        return res

        # res = []
        # res.append(0)
        # for i in range(1, n+1):
        #     curr_bit_cnt = 0
        #     for j in range(18):
        #         tmp = (i >> j) & 1
        #         curr_bit_cnt += 1 if tmp == 1 else 0
        #     res.append(curr_bit_cnt)
        # return res
