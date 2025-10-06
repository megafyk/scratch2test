class Solution:
    def decodeString(self, s: str) -> str:
        # recursion
        # time O(L), L = length of output, space O(n)
        nearest = {}
        st = []
        for i,c in enumerate(s):
            if c == '[':
                st.append(i)
            elif c == ']':
                idx = st.pop()
                nearest[idx] = i
        digits = "0123456789"
        def decode(start,end):
            res = ''
            d = 0
            i = start
            while i < end:
                if s[i] in digits:
                    if d == 0:
                        d = int(s[i])
                    else:
                        d = d * 10 + int(s[i])
                    i += 1
                elif s[i] == '[':
                    res += d * decode(i+1,nearest[i])               
                    d = 0
                    i = nearest[i] + 1
                else:
                    res += s[i]
                    i += 1
            return res
        
        return decode(0, len(s))