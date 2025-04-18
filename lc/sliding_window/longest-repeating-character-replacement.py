class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        # time O(N), space O(1)
        i = j = 0
        counter = [0] * 26
        N = len(s)
        mx_counter = 0
        res = 0
        while j < N:
            ch_idx = ord(s[j]) - ord('A')
            counter[ch_idx] += 1
            mx_counter = max(mx_counter, counter[ch_idx])
            while (j-i+1) - mx_counter > k:
                counter[ord(s[i]) - ord('A')] -= 1
                i += 1
            res = max(res, j-i+1)
            j += 1

        return res