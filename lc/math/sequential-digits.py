class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for i in range(1, 10):
            num = i
            for j in range(i+1, 10):
                num = num*10 + j
                if low <= num <= high:
                    res.append(num)
        return sorted(res)

class Solution1:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_str, high_str = str(low), str(high)
        low_cnt, high_cnt = len(low_str), len(high_str)
        res = []
        for cnt in range(low_cnt, high_cnt + 1):
            for d in range(1, 10):
                cur_cnt = 1
                cur_d = d
                num = d
                finished_num = True
                while cur_cnt < cnt:
                    cur_cnt += 1
                    cur_d += 1
                    if cur_d >= 10:
                        finished_num = False
                        break
                    num = num * 10 + cur_d

                if finished_num and low <= num <= high:
                    res.append(num)
        return res
