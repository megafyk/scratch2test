from collections import deque, Counter

class Solution:

    def pos(self, chr):
        return ord(chr) - ord('a')

    def removeDuplicateLetters(self, s: str) -> str:
        # complextity O(n), mem O(n)

        cnt = Counter(s)
        st = deque()
        seen = set()

        for chr in s:
            cnt[chr] -= 1

            if chr in seen:
                continue
            
            while st and cnt[st[-1]] > 0 and self.pos(st[-1]) > self.pos(chr):
                seen.remove(st.pop())

            st.append(chr)
            seen.add(chr)
        
        return ''.join(st)
            

