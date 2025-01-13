class Solution:
    def minimumLength(self, s: str) -> int:
        # string hashtable
        # time O(n), space O(1)
        hm = defaultdict(int)
        n = len(s)
        res = n
        
        for i in range(n):
            if (hm[s[i]] + 1) == 3:
                res -= 2
                hm[s[i]] -= 2
            hm[s[i]] += 1
        return res
        