class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for h in range(12):
            for m in range(60):
                if h.bit_count() + m.bit_count() == turnedOn:
                    if m < 10:
                        res.append(str(h) + ":" + "0" + str(m))
                    else:
                        res.append(str(h) + ":" + str(m))
        return res
        
class Solution1:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        def backtrack(cnt, cnt_limit, cur, cur_limit, exp):
            if 2 ** exp > cur_limit or cnt > cnt_limit:
                return []
            if cnt == cnt_limit:
                if cur <= cur_limit:
                    return [cur]
                return []
            res = backtrack(cnt, cnt_limit, cur, cur_limit, exp + 1)
            res += backtrack(cnt+1, cnt_limit, cur + (2 ** (exp+1)), cur_limit, exp + 1)
            return res

        for cnt_h in range(4):
            cnt_m = turnedOn - cnt_h
            if cnt_m < 0:
                continue
            hours = backtrack(0, cnt_h, 0, 11, -1)
            mins = backtrack(0, cnt_m, 0, 59, -1)
            for h in hours:
                for m in mins:
                    if m < 10:
                        res.append(str(h) + ":" + "0" + str(m))
                    else:
                        res.append(str(h) + ":" + str(m))
        return res