from typing import List
from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        i = 0
        ans = []
        d = defaultdict()

        while i + 10 <= len(s):
            if d.get(s[i:i + 10]):
                if d.get(s[i:i + 10]) == 1:
                    ans.append(s[i:i + 10])
                d[s[i:i + 10]] += 1
            else:
                d[s[i:i + 10]] = 1
            i += 1

        return ans


s = Solution()
print(s.findRepeatedDnaSequences("AAAAAAAAAAA"))
