class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        slow = fast = 0
        ans = 0
        counter = [0 for _ in range(26)]
        max_count = 0
        while fast < len(s):
            idx = ord(s[fast]) - ord('A')
            counter[idx] += 1
            max_count = max(max_count, counter[idx])
            while fast - slow + 1 - max_count > k:
                counter[ord(s[slow]) - ord('A')] -= 1
                slow += 1
            ans = max(ans, fast - slow + 1)
            fast += 1
        return ans

s = Solution()
print(s.characterReplacement("AABABBA", 1))
print(s.characterReplacement("ABAB", 2))
print(s.characterReplacement("ABAA", 0))
