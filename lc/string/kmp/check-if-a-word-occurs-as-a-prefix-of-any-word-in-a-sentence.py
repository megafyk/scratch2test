class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # kmp haystack & needle
        # time O(n), space O(1)
        m = len(sentence)
        n = len(searchWord)
        pi = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and searchWord[i] != searchWord[j]:
                j = pi[j-1]
            if searchWord[i] == searchWord[j]:
                j += 1
                pi[i] = j
        j = 0
        count = 1
        for i in range(m):
            if i > 0 and sentence[i-1] == " ":
                count += 1
                j = 0
            while j > 0 and sentence[i] != searchWord[j]:
                j = pi[j-1]
            if sentence[i] == searchWord[j]:
                j += 1
            if j == n:
                if i == n-1 or sentence[i-n] == " ":
                    return count
                else:
                    j = 0
        return -1


    # def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
    #     # brute force
    #     # time O(n^2), space O(n)
    #     for idx, word in enumerate(sentence.split(" ")):
    #         if word.startswith(searchWord):
    #             return idx + 1
    #     return -1
