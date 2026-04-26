class Solution:
    def sortVowels(self, s: str) -> str:
        n = len(s)
        cnt = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        first_idx = {}
        for i, c in enumerate(s):
            if c in "aeiou":
                cnt[c] += 1
                if c not in first_idx:
                    first_idx[c] = i
        arr = []
        for c in "aeiou":
            if c in first_idx:
                arr.append([cnt[c], first_idx[c]])
        arr.sort(key=lambda x: (x[0], -x[1]), reverse=True)
        cur = 0
        ns = []
        for c in s:
            if c in "aeiou":
                if arr[cur][0] == 0:
                    cur += 1
                c = s[arr[cur][1]]
                arr[cur][0] -= 1
            ns.append(c)
        return "".join(ns)
