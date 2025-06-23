class Solution:
    def minSwaps(self, s: str) -> int:
        # complexity: time O(n), mem O(1)
        # count number of orphan "]"
        n = len(s)
        orph = 0
        bal = 0
        for ch in s:
            bal += 1 if ch == "[" else -1
            if bal == -1:
                orph += 1
                bal = 1
        return orph
        