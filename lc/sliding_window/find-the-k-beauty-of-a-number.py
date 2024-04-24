class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        str_num = str(num)
        n = len(str_num)
        res = 0
        for i in range(n-k+1):
            cur_win = int(str_num[i:i+k])
            if cur_win != 0 and num % cur_win  == 0:
                res += 1
        return res