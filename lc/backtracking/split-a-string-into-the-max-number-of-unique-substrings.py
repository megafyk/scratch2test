class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        st = deque([(0, set())])
        mx = 0
        while st:
            i, unisub = st.pop()
            if i == len(s): 
                mx = max(mx, len(unisub))
                continue
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if sub in unisub: continue
                new_unisub = set(unisub)
                new_unisub.add(sub)
                st.append((j+1, new_unisub))
        return mx
        
    # def backtrack(self,i, s, unisub):
    #     if i == len(s): return len(unisub)
    #     mx = 0
    #     for j in range(i, len(s)):
    #         sub = s[i:j+1]
    #         if sub in unisub: continue
    #         unisub.add(sub)
    #         mx = max(mx, self.backtrack(j+1, s, unisub))
    #         unisub.remove(sub)
    #     return mx


    # def maxUniqueSplit(self, s: str) -> int:
    #     # backtrack
    #     # time O(2^n), space O(n)
    #     unisub = set()
    #     return self.backtrack(0, s, unisub)