class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # couting + greedy
        # time O(n), space O(n)
        cnt = Counter(words)
        center = False
        longest_p = 0
        for k in list(cnt.keys()):
            rev_k = k[::-1]
            if k != rev_k:
                t = min(cnt[k], cnt[rev_k])
                cnt[k] -= t
                cnt[rev_k] -= t
            else:
                t = cnt[k] // 2
                if cnt[k] % 2 == 1:
                    center = True
                cnt[k] -= t * 2
            longest_p += 4*t
        return longest_p + (1 if center else 0) * 2