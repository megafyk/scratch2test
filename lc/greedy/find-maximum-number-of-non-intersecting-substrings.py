class Solution:
    def maxSubstrings(self, word: str) -> int:
        # greedy
        # time O(w), space O(1)
        n = len(word)
        far = [-1] * 26
        res = 0
        for i,ch in enumerate(word):
            idx = ord(ch) - ord('a')
            if far[idx] == -1:
                far[idx] = i
            else:
                 if i-far[idx]+1 >= 4:
                    res += 1
                    far = [-1] * 26
        return res
                