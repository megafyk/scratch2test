class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # string use stack
        # time O(n), space O(n)
        res = 0
        n = len(s)
        st = deque([-1])
        for i in range(n):
            if s[i] == "(":
                st.append(i)
            else:
                st.pop()
                if len(st) == 0:
                    st.append(i)
                else:
                    res = max(res, i-st[-1])
        return res
