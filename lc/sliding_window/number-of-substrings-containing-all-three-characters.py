class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # sliding window
        # time O(n), space O(1)
        res = 0
        cnt_abc = defaultdict(int)
        n = len(s)
        i = 0
        for j in range(n):
            if s[j] in "abc":
                cnt_abc[s[j]] += 1
            while len(cnt_abc) == 3:
                res += n - j
                if s[j] in "abc":
                    cnt_abc[s[i]] -= 1
                    if cnt_abc[s[i]] == 0:
                        cnt_abc.pop(s[i])
                i += 1
        return res