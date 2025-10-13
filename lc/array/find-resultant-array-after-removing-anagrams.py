class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        res = []
        cnt = [[0] * 26 for _ in range(n)]
        for idx, word in enumerate(words):
            for c in word:
                cnt[idx][ord(c) - ord('a')] += 1
        for i in range(n):
            if i > 0 and cnt[i] == cnt[i-1]:
                continue
            res.append(words[i])
        return res