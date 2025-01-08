class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # string brute force
        # time O(n^2), space O(1)
        res = 0
        n = len(words)
        for i in range(n):
            for j in range(i+1, n):
                l1 = len(words[i])
                l2 = len(words[j])
                if l1 <= l2:
                    prefix = words[j][:l1]
                    suffix = words[j][l2-l1:]
                    if words[i] == prefix and words[i] == suffix:
                        res += 1
        return res