class Solution:
    def compressedString(self, word: str) -> str:
        c_cur = ''
        c_cnt = 0
        comp = ''
        for c in word:
            if c != c_cur:
                if c_cnt != 0:
                    comp += str(c_cnt) + c_cur
                c_cur = c
                c_cnt = 1
            else:
                if c_cnt == 9:
                    comp += str(9) + c_cur
                    c_cnt = 0
                c_cnt += 1
        comp += str(c_cnt) + c_cur
        return comp
