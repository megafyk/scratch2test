class Solution:
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
