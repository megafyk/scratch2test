class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temp = [0] * 26
        for c in s:
            temp[ord(c) - 97] += 1
        for c in t:
            temp[ord(c) - 97] -= 1
        for i in range(26):
            if temp[i] != 0:
                return False
        return True

s = Solution()
print(s.isAnagram("rat", "cat"))
