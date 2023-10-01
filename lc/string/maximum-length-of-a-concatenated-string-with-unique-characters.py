from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:

        dp = [set()]
        ans = 0
        for w in arr:
            t = set(w)
            if len(t) < len(w):
                continue
            for c in dp:
                if t & c:
                    continue
                else:
                    dp.append(t | c)
                    ans = max(ans, len(t | c))
        return ans


s = Solution()
print(s.maxLength(["un", "iq", "ue"]))
print(s.maxLength(["cha","r","act","ers"]))
