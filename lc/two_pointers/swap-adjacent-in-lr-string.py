class Solution:

    def skip(self, s, n, idx):
        while idx < n and s[idx] == "X":
            idx += 1
        return idx

    def canTransform(self, start: str, result: str) -> bool:
        # two pointers
        # time O(N), space O(1)
        n = len(start)
        p1, p2 = 0, 0

        while p1 < n or p2 < n:
            p1 = self.skip(start, n, p1)
            p2 = self.skip(result, n, p2)

            if p1 == n and p2 == n: return True
            if p1 == n or p2 == n: return False
            if start[p1] != result[p2]: return False
            if start[p1] == "R" and p1 > p2: return False
            if start[p1] == "L" and p1 < p2: return False
            p1 += 1
            p2 += 1
        return p1 == p2 == n
