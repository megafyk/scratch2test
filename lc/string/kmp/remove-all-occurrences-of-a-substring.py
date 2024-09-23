from collections import deque
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # complexity: time O(n), mem O(n)
        st = deque()
        st.append(("", 0))

        m = len(part)
        kmp = [0] * m

        j = 0
        for i in range(1, m):
            while j > 0 and part[i] != part[j]:
                j = kmp[j-1]
            if part[i] == part[j]:
                j += 1
                kmp[i] = j
        
        n = len(s)
        i,j = 0,0

        for i in range(n):
            j = st[-1][1]

            while j > 0 and s[i] != part[j]:
                j = kmp[j-1]

            if s[i] == part[j]:
                j += 1               

            st.append((s[i], j))

            if j == m:
                for _ in range(m): st.pop()
                j = kmp[j-1]

        return ''.join(x for x, _ in st)