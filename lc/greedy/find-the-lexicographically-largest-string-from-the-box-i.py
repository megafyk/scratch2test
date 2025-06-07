class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # greedy
        # time O(n^2), space O(n)
        if numFriends == 1: return word
        n = len(word)
        mx_ch = ''
        mx_ch_idx = []
        for i in range(n):
            if word[i] < mx_ch: continue
            elif word[i] == mx_ch: 
                mx_ch_idx.append(i)
            else:
                mx_ch_idx = [i]
                mx_ch = word[i]
        res = ""
        l = n - (numFriends - 1)
        for idx in mx_ch_idx:
            res = max(res, word[idx: min(idx + l, n)])
        return res