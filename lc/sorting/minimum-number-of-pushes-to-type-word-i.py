class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        x = n // 8
        if x >= 3: return 8 + 16 + 24 + 4 * (n-24)
        elif x >= 2: return 8 + 16 + 3 * (n-16)
        elif x >= 1: return 8 + 2 * (n-8)
        return n

class Solution1:
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
