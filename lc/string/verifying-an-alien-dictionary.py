class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        j = 0
        hm = {}
        for idx,chr in enumerate(order):
            hm[chr] = idx
        hm[" "] = -1
        n = len(words)
        j = 1
        for i in range(n-1):
            suffix = " " * abs(len(words[i]) - len(words[j]))
            word1 = words[i] + suffix if len(words[i]) < len(words[j]) else words[i]
            word2 = words[j] + suffix if len(words[i]) > len(words[j]) else words[j]

            for k in range(len(word1)):
                tmp = hm[word1[k]] - hm[word2[k]]
                if tmp < 0:
                    break
                elif tmp > 0:
                    return False
            j += 1
        return True 

