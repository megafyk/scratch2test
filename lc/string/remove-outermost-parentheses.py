from collections import deque


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        q = deque()
        res = ""
        for c in s:
            count += 1 if c == "(" else -1
            if count == 0 and len(q) > 0:
                q.popleft()
                while len(q) != 0:
                    res += q.popleft()
            else:
                q.append(c)
        return res


s = Solution()
print(s.removeOuterParentheses("(()())(())"))
