class Solution:
    def check(self, s):
        vowels = {'a','e','i','o','u'}
        return s[0] in vowels and s[-1] in vowels

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # array prefix sum
        # time O(n), space O(n)
        res = []
        n = len(words)
        prefix = [0] * n

        for i in range(n):
            prefix[i] = prefix[max(0, i-1)] + (1 if self.check(words[i]) else 0)

        for s,e in queries:
            res.append(prefix[e] - (prefix[s-1] if s > 0 else 0))

        return res
