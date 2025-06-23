class Solution:
    def skip_blank(self, s, n, cur):
        while cur < n and s[cur] == '_':
            cur += 1
        return cur

    def canChange(self, start: str, target: str) -> bool:
        # two pointer
        # time O(n), space O(1)
        first = second = 0
        n = len(start)

        while first < n or second < n:
            first = self.skip_blank(start, n, first)
            second = self.skip_blank(target, n, second)

            if first == second == n:
                return True

            if first == n or second == n:
                return False

            if start[first] != target[second]:
                return False

            if start[first] == "L" and second > first:
                return False
            if start[first] == "R" and second < first:
                return False

            first += 1
            second += 1

        return first == second == n
