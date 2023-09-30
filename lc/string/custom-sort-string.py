from collections import defaultdict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1

        list = []

        for c in order:
            tmp = dic[c] * c
            list.append(tmp)
            dic.pop(c)

        for k,v in dic.items():
            list.append(k*v)

        return ''.join(list)

s = Solution()
print(s.customSortString("cba", "abcd"))