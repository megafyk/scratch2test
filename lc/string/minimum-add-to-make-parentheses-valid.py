class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = deque()

        for c in s:
            top = ""
            if st:
                top = st[-1]
            if top == "(" and c == ")":
                st.pop()
            else:
                st.append(c)

        return len(st)