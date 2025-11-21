class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        prefix = []
        prev = defaultdict(list)
        for i in range(n):
            prefix_at_i = list(prefix[-1]) if i > 0 else [0] * 26
            prefix_at_i[ord(s[i]) - ord("a")] += 1
            prefix.append(prefix_at_i)

            if len(prev[s[i]]) == 2:
                prev[s[i]][-1] = i
            else:
                prev[s[i]].append(i)
        
        def count(fr, to):
            res = 0
            for i in range(26):
                res += 1 if (to[i] - fr[i]) > 0 else 0
            return res

        res = 0
        for k, v in prev.items():
            if len(v) == 2:
                first, last = v
                tmp = count(prefix[first], prefix[last-1])
                res += tmp
        return res


class Solution1:
    def countPalindromicSubsequence(self, s: str) -> int:
        # string array
        # time O(n), space O(n)
        l = defaultdict(int)
        r = Counter(s)
        res = set()
        n = len(s)
        for i in range(n):
            mid = s[i]
            r[mid] -= 1
            for k,v in r.items():
                if k in l and v > 0:
                    res.add(k + mid + k)
            l[mid] += 1
        return len(res)
