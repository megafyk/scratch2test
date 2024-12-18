class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # increase monotonic stack
        # time O(n), space O(n)
        n = len(num)
        if k >= n: return "0"

        st = deque()
        cnt = 0
        for d in num:
            while cnt < k and st and int(st[-1]) > int(d):
                st.pop()
                cnt+=1
            st.append(d)
        while cnt < k and st:
            cnt += 1
            st.pop()
        while st and st[0] == "0":
            st.popleft()
        t = ''.join(st)

        return t if len(t) > 0 else "0"
