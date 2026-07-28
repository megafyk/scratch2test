class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # couting sort
        # time O(26 * n), space O(n)
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        half = []
        a = ord('a')
        mid = ''
        for i in range(26):
            if cnt[i] > 0:
                half.append(chr(a + i) * (cnt[i] // 2))
            if cnt[i] % 2:
                mid = chr(a+i)

        left = ''.join(half)
        right = ''.join(half[::-1])
        return left + mid + right
