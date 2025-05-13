class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        # array
        # time O(N), space O(1)
        mod = 10 ** 9 + 7
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        for _ in range(t):
            cnt_z = cnt[-1]
            for i in range(25, 0, -1):
                cnt[i] = cnt[i-1]
                cnt[i-1] = 0
            cnt[0] += cnt_z % mod 
            cnt[1] += cnt_z % mod
            
        return sum(cnt) % mod