class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # 2 pointers
        # time O(n), space O(n)
        n = len(s)
        res = [""] * n
        i = 0
        j = n-1
        def is_abc(ch):
            return "a" <= ch <= "z" or "A" <= ch <= "Z"
        
        while i <= j:
            if not is_abc(s[j]):
                res[j] = s[j]
                j -= 1
            elif not is_abc(s[i]):
                res[i] = s[i]
                i += 1
            else:
                res[i], res[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(res)
