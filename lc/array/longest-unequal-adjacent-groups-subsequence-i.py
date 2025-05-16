class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # array
        # time O(n), space O(n)
        res = [words[0]]
        prev = 0
        for i in range(1, len(groups)):
            if groups[i] != groups[prev]:
                res.append(words[i])
                prev = i
        return res
