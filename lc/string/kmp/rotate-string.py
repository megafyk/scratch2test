class Solution:
    def find(self, needle, haystack):
        n = len(needle)
        pi = [0] * n # longest prefix suffix table
        j = 0
        for i in range(1, n):
            while j > 0 and needle[i] != needle[j]:
                j = pi[j-1]

            if needle[i] == needle[j]:
                j+=1
                pi[i] = j

        m = len(haystack)
        j = 0
        for i in range(m):
            while j > 0 and haystack[i] != needle[j]:
                j = pi[j-1]
            if haystack[i] == needle[j]:
                j+=1
            if j == n: return True
        return False

    def rotateString(self, s: str, goal: str) -> bool:
        # string kmp
        # time O(n), space O(n)
        if len(s) != len(goal): return False
        return self.find(s, goal + goal)
