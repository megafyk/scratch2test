class Solution:
    def minimumPushes(self, word: str) -> int:
        # sorting
        # time O(n), space O(1)
        cnt = [0] * 26
        for c in word:
            i = ord(c) - ord('a')
            cnt[i] += 1
        cnt.sort(reverse=True)
        res = 0
        for i in range(26):
            res += (i//8 + 1) * cnt[i]
        return res
