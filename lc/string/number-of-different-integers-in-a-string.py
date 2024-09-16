class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        # complexity: time O(n), mem O(n)
        s = set()
        t = ''
        for ch in word:
            if not ch.isdigit():
                if len(t) > 0:
                    s.add(int(t))
                t = ''
            else:
                t += ch
        if len(t) > 0: s.add(int(t))
        return len(s)
