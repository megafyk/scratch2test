class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ans = 0

        mask_count = [0] * 1024
        mask_count[0] = 1

        curr = 0
        for c in word:
            curr ^= 1 << (ord(c) - ord('a'))
            # all character count is even
            ans += mask_count[curr]
            # at most 1 character is odd
            for i in range(10):
                new_mask = curr ^ (1 << i)
                ans += mask_count[new_mask]
            mask_count[curr] += 1

        return ans

s = Solution()
print(s.wonderfulSubstrings("ababa"))