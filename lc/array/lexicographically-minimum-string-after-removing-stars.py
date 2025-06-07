class Solution:
    def clearStars(self, s: str) -> str:
        # counter stack
        # time O(26*n), space O(n)
        cur_freq = defaultdict(list)
        res = list(s)
        for i,ch in enumerate(s):
            if ch == "*":
                res[i] = ""
                if cur_freq:
                    t = min(cur_freq)
                    res[cur_freq[t].pop()] = ""
                    if len(cur_freq[t]) == 0:
                        del cur_freq[t]
            else:
                cur_freq[ch].append(i)
        return ''.join(res)