class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        dict1 = {}
        dict2 = {}
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = t[i]
            elif dict1[s[i]] != t[i]:
                return False
            if t[i] not in dict2:
                dict2[t[i]] = s[i]
            elif dict2[t[i]] != s[i]:
                return False

        return True


s = Solution()
print(s.isIsomorphic("foo", "bar"))
print(s.isIsomorphic("badc", "baba"))
