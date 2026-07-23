class Solution:
    def numOfSubsequences(self, s: str) -> int:
        # prefix sum
        # time O(n), space O(n)
        n = len(s)
        prefix_l = [0] * n
        suffix_t = [0] * n
        prefix_l[0] = 1 if s[0] == "L" else 0
        suffix_t[-1] = 1 if s[-1] == "T" else 0
        for i in range(1, n):
            prefix_l[i] = prefix_l[i-1] + (1 if s[i] == "L" else 0)
            suffix_t[n-1-i] = suffix_t[n-i] + (1 if s[n-1-i] == "T" else 0)
        base = 0
        mx_gain = 0
        prefix_lc = suffix_ct = 0
        for i in range(n):
            if s[i] == "C":
                base += prefix_l[i] * suffix_t[i]
                prefix_lc += prefix_l[i]
                suffix_ct += suffix_t[i]
            mx_gain = max(mx_gain, prefix_l[i] * suffix_t[i])

        mx_gain = max(mx_gain, prefix_lc, suffix_ct)
        return base + mx_gain
