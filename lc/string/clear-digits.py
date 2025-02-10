class Solution:
    def clearDigits(self, s: str) -> str:
        # stack
        # time O(n), space O(n)
        st = deque()
        digits = set(['1','2','3','4','5','6','7','8','9','0'])
        for c in s:
            if c in digits:
                st.pop()
            else:
                st.append(c)
        return ''.join(st)