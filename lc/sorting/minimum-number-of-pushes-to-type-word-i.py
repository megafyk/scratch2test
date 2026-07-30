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
            if i < 8:
                res += cnt[i]
            elif 8 <= i < 16:
                res += 2 * cnt[i]
            elif 16 <= i < 24:
                res += 3 * cnt[i]
            else:
                res += 4 * cnt[i]
        return res
