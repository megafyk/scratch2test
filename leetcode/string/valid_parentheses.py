from collections import deque


class Solution:     
    def isValid(self, s: str) -> bool:
        q = deque()
        pair = ["()", "{}", "[]"]
        for c in s:
            if c == '{' or c == '[' or c == '(':
                q.append(c)
            elif c == '}' or c == ']' or c == ')':
                if len(q) == 0 or q.pop() + c not in pair:
                    return False
        return len(q) == 0


s = Solution()
print(s.isValid("()"))
