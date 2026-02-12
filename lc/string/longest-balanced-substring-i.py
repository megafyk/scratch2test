class Solution:
    def longestBalanced(self, s: str) -> int:
        # string
        # time O(26*n*n), space O(n)
        n = len(s)
        longest = 0
        for i in range(n):
            cnt = defaultdict(int)
            for j in range(i, n):
                cnt[s[j]] += 1
                freq = -1
                balanced = True
                for v in cnt.values():
                    if freq == -1:
                        freq = v
                    else:
                        if v != freq:
                            balanced = False
                            break
                if balanced:
                    longest = max(longest, j-i+1)
        return longest 
