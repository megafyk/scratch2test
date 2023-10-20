from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        if len(s) < len(p):
            return ans

        d_p = {}
        d_s = {}

        for i in range(len(p)):
            d_p[p[i]] = d_p[p[i]] + 1 if p[i] in d_p else 1
            d_s[s[i]] = d_s[s[i]] + 1 if s[i] in d_s else 1

        left = 0
        right = left + len(p) - 1

        while right < len(s):
            if d_s == d_p:
                ans.append(left)
            if d_s[s[left]] == 1:
                d_s.pop(s[left])
            else:
                d_s[s[left]] -= 1
            left += 1
            right += 1

            if right < len(s):
                if s[right] in d_s:
                    d_s[s[right]] += 1
                else:
                    d_s[s[right]] = 1

        return ans


s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))
print(s.findAnagrams("aaa", "aaa"))
print(s.findAnagrams("abab", "ab"))
