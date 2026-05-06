class Solution:
    def find(self, needle: str, haystack: str) -> bool:
        """
        Knuth-Morris-Pratt (KMP) substring search.

        Determines whether `needle` exists as a substring of `haystack`.

        Algorithm overview:
        1. Build the *failure function* (pi table) for `needle`.
           pi[i] = length of the longest proper prefix of needle[0..i]
           that is also a suffix of needle[0..i].
        2. Scan `haystack` using `j` as a pointer into `needle`.
           On a mismatch, fall back via pi instead of restarting from 0,
           guaranteeing each character is visited at most twice overall.

        Args:
            needle:   The pattern to search for.
            haystack: The text to search within.

        Returns:
            True if needle is found in haystack, False otherwise.

        Complexity:
            Time  O(n + m)  where n = len(needle), m = len(haystack)
            Space O(n)      for the pi table
        """
        n = len(needle)
        pi = [0] * n  # failure function (longest prefix-suffix lengths)
        # Phase 1: build the pi (failure function) table
        j = 0
        for i in range(1, n):
            while j > 0 and needle[i] != needle[j]:
                j = pi[j - 1]  # fall back using previously computed values
            if needle[i] == needle[j]:
                j += 1
                pi[i] = j

        # Phase 2: search haystack for needle
        m = len(haystack)
        j = 0
        for i in range(m):
            while j > 0 and haystack[i] != needle[j]:
                j = pi[j - 1]  # mismatch: reuse the longest valid prefix
            if haystack[i] == needle[j]:
                j += 1
            if j == n:  # full match found
                return True
        return False
