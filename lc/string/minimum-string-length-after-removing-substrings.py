class Solution:
    def minLength(self, s: str) -> int:
        st = deque([""])
        for c in s:
            top = st[-1]
            if top + c == "AB" or top + c == "CD":
                st.pop()
            else:
                st.append(c)
        st.popleft()
        return len(st)