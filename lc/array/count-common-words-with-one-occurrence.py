class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        # time O(n), space O(n+m)
        freq1 = Counter(words1)
        freq2 = Counter(words2)

        res = 0
        for k,v in freq1.items():
            if v == 1 and freq2[k] == 1:
                res += 1
        return res