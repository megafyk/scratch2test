class Solution:
    def maxScore(self, s: str) -> int:
        # time O(n), space O(1)
        freq = Counter(s)

        left = 1 if s[0] == "0" else 0
        right = freq["1"] - (1 if s[0] == "1" else 0)
        res = left + right
        for i in range(1, len(s) - 1):
            if s[i] == "1":
                right -= 1
            else:
                left += 1
            res = max(res, left + right)
        return res
