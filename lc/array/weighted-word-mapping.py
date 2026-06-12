class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        # array
        # time O(w*len(w)), space O(w)
        n = len(words)
        res = [""] * n
        start = ord("a")
        for i, w in enumerate(words):
            weight = 0
            for c in w:
                weight += weights[ord(c) - start]
            res[i] = chr(start + (25 - weight % 26))
        return "".join(res)
