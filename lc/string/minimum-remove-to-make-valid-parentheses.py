from collections import deque

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = deque()
        s_arr = list(s)

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if len(stack) == 0:
                    s_arr[i] = ''
                else:
                    stack.pop()

        for e in stack:
            s_arr[e] = ''

        return ''.join(s_arr)

s = Solution()
print(s.minRemoveToMakeValid("lee(t(c)o)de)"))