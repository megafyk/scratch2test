class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d_t = {}
        for c in t:
            if c not in d_t:
                d_t[c] = 0 
            d_t[c] += 1

        
        win_count = 0
        min_len = len(s) + 1
        
        slow, fast, head = 0,0,0
        
        while fast < len(s):
            if s[fast] in d_t:
                if d_t[s[fast]] > 0:
                    win_count += 1
                d_t[s[fast]] -= 1

            fast += 1
            # window match t
            while win_count == len(t):
                if fast - slow < min_len:
                    min_len = fast - slow
                    head = slow


                if s[slow] in d_t:
                    d_t[s[slow]] += 1
                    if d_t[s[slow]] > 0:
                        win_count -= 1
                slow += 1
            
        if min_len == len(s) + 1:
            return ''



        return s[head: head + min_len]

s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
print(s.minWindow("a", "a"))
print(s.minWindow("a", "aa"))
print(s.minWindow("bdab", "ab"))
