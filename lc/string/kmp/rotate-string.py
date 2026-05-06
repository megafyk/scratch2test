class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # kmp
        # time O(n), space O(n)
        if len(s) != len(goal):
            return False
        n = len(s)
        lps = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and goal[i] != goal[j]:
                j = lps[j - 1]
            if goal[i] == goal[j]:
                j += 1
                lps[i] = j

        s += s
        j = 0
        for i in range(2 * n):
            while j > 0 and s[i] != goal[j]:
                j = lps[j - 1]
            if s[i] == goal[j]:
                j += 1
            if j == n:
                return True
        return False


class Solution1:
    def find(self, needle, haystack):
        n = len(needle)
        pi = [0] * n  # longest prefix suffix table
        j = 0
        for i in range(1, n):
            while j > 0 and needle[i] != needle[j]:
                j = pi[j - 1]

            if needle[i] == needle[j]:
                j += 1
                pi[i] = j

        m = len(haystack)
        j = 0
        for i in range(m):
            while j > 0 and haystack[i] != needle[j]:
                j = pi[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == n:
                return True
        return False

    def rotateString(self, s: str, goal: str) -> bool:
        # string kmp
        # time O(n), space O(n)
        if len(s) != len(goal):
            return False
        return self.find(s, goal + goal)


class Solution2:
    def rotateString(self, s: str, goal: str) -> bool:
        # brute force
        # time O(n^2), space O(1)
        if len(s) != len(goal):
            return False
        n = len(s)
        s += s
        for i in range(n):
            if s[i : i + n] == goal:
                return True
        return False
